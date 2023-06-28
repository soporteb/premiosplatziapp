import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

#Models
#Views

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30) #30 dias en el futuro
        future_question = Question(question_text= "¿Quien es el mejor Course Director de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False) #False porque la fecha de publicacion es en el futuro


