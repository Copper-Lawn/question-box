from rest_framework import viewsets, permissions, renderers
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from django.views.generic.base import TemplateView


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class QuestionsPageView(TemplateView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    template_name = 'stackunderflow/question.html'

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['given_question'] = Question.objects.filter(id=kwargs['pk'])
        return context

    # def get_context_data(self, **kwargs):
    #     context = super(QuestionsPageView, self).get_context_data(**kwargs)
    #     context['questions_list'] = Question.objects.all()
    #     return context


class AnswersViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
