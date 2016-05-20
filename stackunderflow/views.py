from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)





from django.views.generic.base import TemplateView


class ProfileView(TemplateView):
    template_name = "stackunderflow/profile.html"
