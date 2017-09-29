from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.http import HttpResponse
# from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from django.utils import timezone
from .models import Item
import json
from django.core import serializers


# Create your views here.

@login_required
def item_create(request):
    initial_data = {
        'created_date': timezone.now().date(),
    }
    form = ItemForm(request.POST or None, initial=initial_data)
    if request.method == 'POST':
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, "Expense added.")
            return redirect("item_create")

    context = {
        'form': form
    }
    return render(request, 'items/item_edit.html', context)


@login_required
def item_edit(request, pk):
    item_data = get_object_or_404(Item, id=pk)
    form = ItemForm(data=request.POST or None, instance=item_data)
    if request.method == 'POST':
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, "Item %s edited" % (item.name))
            return redirect('item_list')
    context = {
        'form': form
    }
    return render(request, 'items/item_edit.html', context)


@login_required
def item_list(request):
    item_list = Item.objects.all().order_by("name")
    per_page = 10
    paginator = Paginator(item_list, per_page)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'items/item_list.html', {'items': items})


@login_required
def item_delete(request, pk):
    try:
        item = Item.objects.get(user=request.user, id=pk)  # item is a database
    except Item.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        item.delete()
        # messages.success(request, "Transaction %s deleted." % item.title)
        return redirect('item_list')

    context = {
        'item': item
    }
    return render(request, 'items/delete.html', context)


@login_required
def item_unit_price(request, pk):
    if request.is_ajax():
        data = Item.objects.get(id=pk)
        price = data.unit_price
        return HttpResponse(price)
