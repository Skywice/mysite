# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),  # ^ $ 分别匹配字符串的开头和结尾
    # ex: /polls/5
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),  # 对应的是参数的名称?
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/votes/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]