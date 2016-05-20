from rest_framework import viewsets, permissions, renderers
from .models import Question, Answer, Keyword
from .serializers import QuestionSerializer, AnswerSerializer, KeywordSerializer
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User



""" User views """


class HomeView(TemplateView):
    template_name = "stackunderflow/home.html"


class QuestionsPageView(TemplateView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    template_name = 'stackunderflow/question.html'

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


    def get_queryset(self):
        order_by = self.request.GET.get('sort', 'title')
        return Question.objects.all().order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['given_question'] = Question.objects.filter(id=kwargs['pk'])
        return context


class CreateAccountView(TemplateView):
    template_name = "stackunderflow/register.html"
    # queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_list'] = User.objects.all()
        return context


class ProfileView(TemplateView):
    template_name = "stackunderflow/profile.html"


""" API Endpoint views """



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


class KeywordViewSet(viewsets.ModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
