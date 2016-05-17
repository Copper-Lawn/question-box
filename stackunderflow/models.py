from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    answers = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True)


class Answer(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User)
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
