from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UnitForm
from .models import Unit
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages


# Create your views here.
@login_required
def unit_create(request):
    """
        Add New Unit
    """
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.user = request.user
            unit.save()
            messages.success(request, 'Successfully saved new unit.')
            return redirect('unit_create')
    else:
        form = UnitForm()
    return render(request, 'units/unit_edit.html', {'form': form})


@login_required
def unit_edit(request, pk):
    unit = get_object_or_404(Unit, id=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.user = request.user
            unit.save()
            return redirect('home_page')
    else:
        form = UnitForm(instance=unit)
    return render(request, 'units/unit_edit.html', {'form': form})


@login_required
def unit_delete(request, pk):
    '''
        Here at first it is redirected to delete confirmation page where it is confirmed.

    '''
    try:
        unit = request.user.Unit.get(pk=pk)  # Unit is a database
    except Unit.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        unit.delete()
        # messages.success(request, "Transaction %s deleted." % unit.title)
        return redirect('unit_list')

    context = {
        'unit': unit
    }
    return render(request, 'units/delete.html', context)


@login_required
def unit_list(request):
    unit_list = Unit.objects.all().order_by("name")
    per_page = 10
    paginator = Paginator(unit_list, per_page)
    page = request.GET.get('page')

    try:
        units = paginator.page(page)
    except PageNotAnInteger:
        units = paginator.page(1)
    except EmptyPage:
        units = paginator.page(paginator.num_pages)

    return render(request, 'units/unit_list.html', {'units': units})
