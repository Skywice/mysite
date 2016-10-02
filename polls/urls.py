# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views_old

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
    url(r'^$', views_old.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views_old.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views_old.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views_old.vote, name='vote'),

]