from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransactionForm
from django.contrib import messages
from .models import Transaction
# from items.models import Item
from datetime import datetime
from customers.forms import CustomerForm
from .templatetags.datefilter import hour_limit


# Create your views here.

@login_required
def transaction_create(request):
    c_form = CustomerForm(request.POST or None)
    form = TransactionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.total_price = transaction.item.unit_price * transaction.quantity
            transaction.created_date = datetime.now()
            transaction.created_hour = datetime.now()
            transaction.user = request.user
            if c_form.is_valid():
                customer = c_form.save(commit=False)
                if len(customer.name) != 0:
                    customer.user = request.user
                    customer.save()
                    transaction.customer_id = customer.id
                    transaction.save()
                    messages.success(request, "Transaction saved successfully with new customer")
                    return redirect('transaction_create')
            transaction.save()
            messages.success(request, "Transaction saved.")
            return redirect('transaction_create')
    context = {
        'form': form,
        'customer_form': c_form,
    }
    return render(request, 'transactions/transaction_edit.html', context)


@login_required
def transaction_list(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    item_name = request.GET.get('item_name')
    form = TransactionForm()
    if start_date and end_date:
        transaction = Transaction.objects.filter(user=request.user,
                                                 created_date__range=(str(start_date), str(end_date))).order_by(
            'created_date')
    elif item_name:
        transaction = Transaction.objects.filter(user=request.user, item=item_name).order_by('created_date')
    else:
        transaction = Transaction.objects.filter(user=request.user).order_by("created_date")
    per_page = 10
    paginator = Paginator(transaction, per_page)
    page = request.GET.get('page')

    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        transactions = paginator.page(1)
    except EmptyPage:
        transactions = paginator.page(paginator.num_pages)

    if start_date and end_date:
        context = {
            'transactions': transactions,
            'start_date': start_date,
            'end_date': end_date,
            'form': form
        }
    else:
        context = {
            'transactions': transactions,
            'item_name': item_name,
            'form': form
        }

    return render(request, 'transactions/transaction_list.html', context)


@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, id=pk, user=request.user)
    if hour_limit(transaction.valid_date):
        form = TransactionForm(data=request.POST or None, instance=transaction)
        if request.method == 'POST':
            if form.is_valid():
                transaction = form.save(commit=False)
                transaction.total_price = transaction.item.unit_price * transaction.quantity
                transaction.user = request.user
                transaction.save()
                return redirect('transaction_list')

        context = {
            'form': form,
        }
        return render(request, 'transactions/transaction_edit.html', context)

    return render(request, 'transactions/error_msg.html', {'transaction': transaction.id})


@login_required
def transaction_delete(request, pk):
    try:
        transaction = Transaction.objects.get(user=request.user, id=pk)  # item is a database
    except Transaction.DoesNotExist:
        raise Http404()

    if hour_limit(transaction.valid_date):
        if request.method == 'POST':
            transaction.delete()
            return redirect('transaction_list')

        context = {
            'transaction': transaction
        }
        return render(request, 'transactions/delete.html', context)
    return render(request, 'transactions/error_msg.html')