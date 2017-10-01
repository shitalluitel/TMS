from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransactionForm
from django.contrib import messages
from .models import Transaction
import datetime

# Create your views here.

@login_required
def transaction_create(request):
    form = TransactionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.total_price = transaction.Transaction.unit_price * transaction.quantity
            transaction.user = request.user
            transaction.created_date = datetime.datetime.today().strftime('%Y-%m-%d')
            transaction.save()
            messages.success(request, "Successful transaction")
            return redirect('transaction_create')
    context = {
        'form': form
    }
    return render(request, 'transactions/transaction_edit.html', context)


@login_required
def transaction_list(request):
    transaction = Transaction.objects.all().order_by("created_date")
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    item_name = request.GET.get('item_name')
    print("start date: %s \n end date: %s" % (start_date, end_date))

    per_page = 10
    paginator = Paginator(transaction, per_page)
    page = request.GET.get('page')

    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        transactions = paginator.page(1)
    except EmptyPage:
        transactions = paginator.page(paginator.num_pages)

    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})


@login_required
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, id=pk)
    form = TransactionForm(data=request.POST or None, instance=transaction)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.total_price = transaction.Transaction.unit_price * transaction.quantity
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Successful transaction")
            return redirect('transaction_list')

    context = {
        'form': form
    }
    return render(request, 'transactions/transaction_edit.html', context)
