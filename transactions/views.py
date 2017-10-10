from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransactionForm
from django.contrib import messages
from .models import Transaction
# from items.models import Item
from datetime import datetime


# Create your views here.

@login_required
def transaction_create(request):
    form = TransactionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.total_price = transaction.item.unit_price * transaction.quantity
            transaction.created_date = datetime.now()
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Successful transaction")
            return redirect('transaction_create')
    context = {
        'form': form
    }
    return render(request, 'transactions/transaction_edit.html', context)


@login_required
def transaction_list(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    item_name = request.GET.get('item_name')
    form = TransactionForm()
    if start_date and end_date:
        transaction = Transaction.objects.filter(created_date__range=(str(start_date),str(end_date))).order_by('created_date')
    elif item_name:
        transaction = Transaction.objects.filter(item=item_name).order_by('created_date')
    else:
        transaction = Transaction.objects.all().order_by("created_date")
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
    transaction = get_object_or_404(Transaction, id=pk)
    form = TransactionForm(data=request.POST or None, instance=transaction)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.total_price = transaction.item.unit_price * transaction.quantity
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Successful transaction")
            return redirect('transaction_list')

    context = {
        'form': form
    }
    return render(request, 'transactions/transaction_edit.html', context)
