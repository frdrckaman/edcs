from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import DemographicForm
from .models import Demographic
from django.http import HttpResponse


def DemographicCreate(request):
    if request.method == 'POST':
        form = DemographicForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect(reverse(''))
            return HttpResponse('Successfully Saved')

    else:
        form = DemographicForm()
    return render(request, 'edcs_rab002/edcs_rab002_home.html', {'form': form})


def DemographicEdit(request, pk=None):
    demographic = get_object_or_404(Demographic, pk=pk)
    if request.method == 'POST':
        form = DemographicForm(request.POST, instance=demographic)
        if form.is_valid():
            form.save()
            return redirect('edcs_rab002/DemographicEdit')
    else:
        form = DemographicForm(instance=demographic)
    return render(request, 'edcs_rab002/edcs_rab002_edit.html', {'form': form, 'demographic': demographic})

