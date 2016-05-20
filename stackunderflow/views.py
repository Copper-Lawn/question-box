from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User


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


class CreateAccountView(TemplateView):
    template_name = "stackunderflow/register.html"
    # queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_list'] = User.objects.all()
        return context















# def register(request):
#     if request.method == 'POST':
#         user_form = UserCreationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save()
#             return HttpResponseRedirect("/board/")
#         else:
#             print(user_form.errors)
#     else:
#         user_form = UserCreationForm()
#
#     context = {'user_form': user_form}
#     return render(request, "registration/register.html", context)
