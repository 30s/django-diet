# encoding: utf8

from django.test import TestCase

from diet.views import *
from diet.models import *


class DietManagerTest(TestCase):

    def setUp(self):
        self.dm = DietManager()

    def test_record(self):
        text = self.dm.record_diet(u'牛奶', 'user')
        # use logging
        print text
        self.assertTrue(len(Diet.objects.all()), 1)

        text = self.dm.record_diet('week', 'user')
        # use logging
        print text
