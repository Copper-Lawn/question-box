from rest_framework import viewsets
from .models import Question, Answer, Keyword
from .serializers import QuestionSerializer, AnswerSerializer, KeywordSerializer
from django.views.generic.base import TemplateView


""" User views """


class HomeView(TemplateView):
    template_name = "stackunderflow/home.html"


class QuestionDetailView(TemplateView):
    template_name = "stackunderflow/home.html"


class CreateAccountView(TemplateView):
    template_name = "stackunderflow/home.html"


class ProfileView(TemplateView):
    template_name = "stackunderflow/profile.html"


""" API Endpoint views """


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        order_by = self.request.GET.get('sort', 'title')
        return Question.objects.all().order_by(order_by)


class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
