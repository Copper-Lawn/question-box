from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, editable=False)
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    answers = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True)
    keywords = models.ManyToManyField('Keyword', null=True, default="")


class Answer(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, editable=False)
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


class Keyword(models.Model):
    keyword = models.CharField(max_length=20, default="")

    def __unicode__(self):
        return self.keyword
