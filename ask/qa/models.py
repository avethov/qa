from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Page, Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):
    def new(self):
        question_list = Question.objects.all().order_by('-added_at')

        return question_list

    def popular(self):
        question_list = Question.objects.all().order_by('-rating')

        return question_list

    def pagination(self,
                   list,
                   page,
                   limit=10):

        paginator = Paginator(list,
                              limit)

        try:
            questions = paginator.page(page)
        except PageNotAnInteger:
            questions = paginator.page(1)
        except EmptyPage:
            questions = paginator.page(paginator.num_pages)

        return questions


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="user_question_related")
    likes = models.ManyToManyField(User)
    objects = QuestionManager()

    def __str__(self):
        return '%s' % self.title

    def get_url(self):
        return reverse('question-details',
                       args=(self.id,))


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)