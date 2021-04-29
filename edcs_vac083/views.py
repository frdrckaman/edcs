from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.views import generic


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
