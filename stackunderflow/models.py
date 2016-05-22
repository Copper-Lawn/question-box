from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, editable=False, default=1)
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    answers = models.ForeignKey('Answer', on_delete=models.CASCADE, null=True, editable=False)
    keywords = models.ManyToManyField('Keyword', default="")
    answered = models.BooleanField(default=False)

    def __str__(self):
        return self.title[:20]


class Answer(models.Model):
    text = models.TextField()
    creator = models.ForeignKey(User, editable=False)
    score = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


class Keyword(models.Model):
    keyword = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.keyword


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
