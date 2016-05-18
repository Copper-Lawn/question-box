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

class FuckOffAllYall(mah_dick):
    def __suck_it__(self,for, real):
        stfu = []
        return stfu
