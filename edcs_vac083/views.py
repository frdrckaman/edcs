from edcs_vac083.forms import DemographicForm
from .models import Demographic
from django.shortcuts import render, redirect, get_object_or_404


def DemographicView(request):
    form = DemographicForm()
    return render(request, 'edcs_vac083/edcs_vac083_home.html', {'form': form})


def DemographicCreate(request):
    if request.method == 'POST':
        form = DemographicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edcs_dashboard:home')

    else:
        form = DemographicForm()
    return render(request, 'edcs_vac083/edcs_vac083_enter_data.html', {'form': form})


def DemographicEdit(request, pk=None):
    demographic = get_object_or_404(Demographic, pk=pk)
    if request.method == 'POST':
        form = DemographicForm(request.POST, instance=demographic)
        if form.is_valid():
            form.save()
            return redirect('edcs_vac083:DemographicCreate')
    else:
        form = DemographicForm(instance=demographic)
    return render(request, 'edcs_vac083/edcs_vac083_edit.html', {'form': form, 'demographic': demographic})
