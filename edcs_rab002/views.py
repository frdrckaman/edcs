from django.shortcuts import render, redirect
from .forms import DemographicForm


def DemographicCreate(request):
    if request.method == 'POST':
        form = DemographicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edcs_rab002/DemographicCreate')
    else:
        form = DemographicForm()
    return render(request, 'edcs_rab002/edcs_rab002_home.html', {'form': form})
