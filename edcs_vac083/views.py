from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views import generic
from django.shortcuts import render
from edcs_vac083.forms import DemographicForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Demographic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# def edcs_vac083_home(generic.ListView):
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#     # return HttpResponse("Hello, world. You're at the Home Page.")
#
# def edcs_vac083_home(request):
#      return HttpResponse("Hello, world. You're at the Home Page.")


def edcs_vac083Home(request):
    # template_name = 'edcs_vac083/edcs_vac083_home.html'
    # context_object_name = 'latest_question_list'
    return HttpResponse('HELO HELO')


# def DemographicView(request):
#     if request.method == "POST":
#         form = DemographicForms(request.POST)
#         if form.is_valid():
#             # Do something with the form data like send an email.
#             return HttpResponseRedirect(reverse('some-form-success-view'))
#     else:
#         form = DemographicForms()
#
#     return render(request, 'demographicForm.html', {'form': form})


# class DemographicView(CreateView):
#     model = DemographicForm
#     # fields = ['subject_initials', 'subject_id', 'visit_date', 'visit_code',
#     #           'gender', 'race', 'dob', 'years', 'months', 'residence', 'phone',
#     #           'literate', 'education', 'address', 'coordinator_initials',
#     #           'coordinator_time', 'reviewer_initials', 'reviewer_time']
#     # template_name = 'edcs_vac083/edcs_vac083_enter_data.html'
#     # form_class = DemographicForm
#     # success_url = '/thanks/'
#
#     # def form_valid(self, form):
#     #     # This method is called when valid form data has been POSTed.
#     #     # It should return an HttpResponse.
#     #     form.send_email()
#     #     return super().form_valid(form)
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)


# class DemographicView(View):

    # def get(self, request):
    #     form = DemographicForm()
    #     return render(request, 'edcs_vac083/edcs_vac083_enter_data.html', {'form': form})


class DemographicView(CreateView):
    model = Demographic
    fields = ['subject_initials', 'subject_id', 'visit_date', 'visit_code',
                'gender', 'race', 'dob', 'years', 'months', 'residence', 'phone',
                'literate', 'education', 'address', 'coordinator_initials',
                'coordinator_time', 'reviewer_initials', 'reviewer_time']
    template_name = 'edcs_vac083/edcs_vac083_enter_data.html'
    success_url = reverse_lazy('edcs_vac083/edcs_vac083_home.html')
