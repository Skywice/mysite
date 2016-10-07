# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

"""
makemigrations 生成转移策略文件
migration 执行转移策略
sqlmigrate 显示转移过程中数据库代码
"""

# two models Questions and Answers
@python_2_unicode_compatible #only if you need to support python2 just like this
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 通过__str__进行分辨
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        # 当前时间
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now  # 是否发布一天以上

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 外键
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_txt
