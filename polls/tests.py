# -*- conding:utf-8 -*-

import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.
class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_quesion(self):
        """
        was_published_recently() should reture False for questions whose pub_date is
        in the future.
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
