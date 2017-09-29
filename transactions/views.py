from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TransactionForm
from django.contrib import messages


# Create your views here.

@login_required
def transaction_create(request):
    form = TransactionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.total_price = transaction.unit_price * transaction.quantity
            transaction.user = request.user
            transaction.save()
            messages.success(request, "Successful transaction")
            return redirect('transaction_create')
    context = {
        'form': form
    }
    return render(request, 'transactions/transaction_edit.html', context)

