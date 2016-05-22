from rest_framework import viewsets, permissions, renderers
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import Question, Answer, Keyword, Owner
from .serializers import QuestionSerializer, AnswerSerializer, KeywordSerializer
from .forms import QuestionForm


""" User views """


class HomeView(TemplateView):
    template_name = "stackunderflow/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        context['keywords'] = Keyword.objects.all()
        context['form'] = QuestionForm()
        return context

    def get_queryset(self):
        order_by = self.request.GET.get('sort', 'title')
        return Question.objects.all().order_by(order_by)

    def post(self, request):
        if request.user.is_authenticated():
            form = QuestionForm(request.POST)
            question = form.save(commit=False)
            question.creator = request.user
            question.creator.owner.score += 5
            question.save()
            question.creator.owner.save()
            for word in request.POST.getlist('keywords'):
                key = Keyword.objects.get(keyword=word)
                question.keywords.add(key)
            question.save()

            return redirect('/question/' + str(question.id))

        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                return redirect('/home/')


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


# class CreateAccountView(TemplateView):
#     template_name = "stackunderflow/register.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users_list'] = User.objects.all()
#         return context

def create_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            owner = Owner(user=user)
            owner.save()
            return redirect('/account/profile/{}/'.format(request.user.user_id))
        else:
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'stackunderflow/register.html', context={'form': form})


class ProfileView(TemplateView):
    template_name = "stackunderflow/profile.html"


def log_out(request):
    logout(request)
    return redirect("/home/")


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
