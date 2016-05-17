from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        print("Trying to set user :( :", self.request.user.id)
        serializer.save(creator=self.request.user)


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
