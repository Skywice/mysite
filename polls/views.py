# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')  # 直接从template中进行寻找
    context = {
        'latest_question_list':latest_question_list
    }
    return HttpResponse(template.render(context, request))
# just write more views
# three functions: detail and results of each question
# vote for choices for each question
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html', {'question': question})

def results(request, question_id):
    response = 'You\'re looking at the result of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You\'re voting on question %s.' % question_id)

