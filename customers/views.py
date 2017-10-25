from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.utils import timezone
from django.core.validators import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm
from .models import Customer
from django.urls import reverse


# Create your views here.
@login_required
def customer_create(request):
    initial_data = {
        'created_date': timezone.now().date()
    }
    form = CustomerForm(request.POST or None, initial=initial_data)
    if request.method == 'POST':
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            messages.success(request, "Customer %s added" % (customer.name))
            return redirect('customer_create')
            # raise form.ValidatioError(_("Username already exist."))
    context = {
        'form': form,
    }

    return render(request, 'customer/customer_edit.html', context)


@login_required
def customer_edit(request, pk):
    customer_data = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer_data)
    if not customer_data.name.lower() == 'cash':
        if request.method == 'POST':
            if form.is_valid():
                customer = form.save()
                messages.success(request, "Customer %s edited." % (customer.name))
                return redirect('customer_create')

        context = {
            'form': form,
        }

        return render(request, 'customer/customer_edit.html', context)
    else:
        return render(request, 'customer/delete.html', {'text': 'edit'})


@login_required
def customer_soft_delete(request, pk):
    # try:
    customer_data = get_object_or_404(Customer, user=request.user, pk=pk)
    # except customer_data.DoesNotExist:
    #     return Http404

    if not customer_data.name.lower() == 'cash':
        if request.method == "POST":
            customer_data.is_deleted = True
            customer_data.save()
            return redirect('customer_list')

        context = {
            "customer_data": customer_data,
            "text": "Trash"
        }

        return render(request, 'customer/delete.html', context)
    else:
        return render(request, 'customer/delete.html', {'text': 'delete'})


@login_required
def customer_restore(request, pk):
    try:
        customer_data = Customer.objects.get(user=request.user, pk=pk)
    except customer_data.DoesNotExist:
        return Http404

    if request.method == "POST":
        customer_data.is_deleted = False
        customer_data.save()
        return redirect('customer_list')

    context = {
        "customer_data": customer_data,
        "text": "Restore",
    }

    return render(request, 'customer/delete.html', context)


@login_required
def customer_delete(request, pk):
    try:
        customer_data = Customer.objects.get(user=request.user, pk=pk)
    except customer_data.DoesNotExist:
        return Http404

    if not customer_data.name.lower() == "cash":
        if request.method == "POST":
            customer_data.delete()
            return redirect(reverse('customer_list') + '?trash=True')

        context = {
            "customer_data": customer_data,
            "text": 'Delete'
        }

        return render(request, 'customer/delete.html', context)

    else:
        return render(request, 'customer/delete.html', {'text': 'delete'})


@login_required
def customer_list(request):
    trash = request.GET.get("trash")
    if trash:
        customer_list_data = Customer.objects.filter(is_deleted=True).order_by("name")
    else:
        customer_list_data = Customer.objects.filter(is_deleted=False).order_by("name")
    per_page = 10
    paginator = Paginator(customer_list_data, per_page)
    page = request.GET.get('page')

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    context = {
        'customers': customers,
        'trash': trash
    }

    return render(request, 'customer/customer_list.html', context)
