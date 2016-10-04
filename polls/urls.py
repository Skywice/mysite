# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'polls'
'''
精简之前的UrlConf
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
'''
# 修改之后
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # 直接就被成为pk 在generic view中
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]