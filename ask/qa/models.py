from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField
    text = models.TextField
    added_at = models.DateField
    rating = models.IntegerField
    author = models.OneToOneField(User, related_name="user_question_related")
    likes = models.ManyToManyField(User)
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField
    added_at = models.DateField
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User)


class QuestionManager(models.Model):
    def new(self):
        pass
    
    def popular(self):
        pass