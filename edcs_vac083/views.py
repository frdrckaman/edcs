from django.shortcuts import render
from django.http import HttpResponse


def edcs_vac083_home(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    return HttpResponse("Hello, world. You're at the Home Page.")