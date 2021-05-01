from edcs_vac083.forms import DemographicForm
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from edcs_vac083.models import Demographic


class DemographicView(ListView):
    model = Demographic
    template_name = 'edcs_vac083/edcs_vac083_view.html'


class edcs_vac083_home(ListView):
    model = Demographic
    template_name = 'edcs_vac083/edcs_vac083_home.html'


class edcs_vac083_visits(ListView):
    model = Demographic
    template_name = 'edcs_vac083/edcs_vac083_visits.html'


def DemographicCreate(request):
    if request.method == 'POST':
        form = DemographicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edcs_dashboard:home')

    else:
        form = DemographicForm()
    return render(request, 'edcs_vac083/edcs_vac083_enter_data.html', {'form': form})


def edcs_vac083_count(request):
    demographicCount = Demographic.objects.count()
    return render(request, 'edcs_vac083/edcs_vac083_home.html',
    {
        'demographicCount' : demographicCount,
    }
    )


