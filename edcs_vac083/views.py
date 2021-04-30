from edcs_vac083.forms import DemographicForm
from django.shortcuts import render, redirect


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
