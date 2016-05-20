from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, editable=False)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    answers = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True)
    keywords = models.CharField(max_length=250, blank=True)


class Answer(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, editable=False)
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

# class Creator(models.Model):
#     user_score = models.IntegerField(default=0)
#     answer_score = models.IntegerField(default=0)
#     user = models.ForeignKey(users)#I don't know what goes in here
