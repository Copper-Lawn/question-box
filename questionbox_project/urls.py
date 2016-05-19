from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from stackunderflow import views

router = routers.DefaultRouter()
router.register(r'api/questions', views.QuestionsViewSet)
router.register(r'api/answers', views.AnswersViewSet)

app_name = 'stackunderflow'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    # url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionDetailView.as_view()),
    # url(r'^account/create/$', views.CreateAccountView.as_view()),
    # url(r'^account/profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view()),
    url(r'^admin/', include(admin.site.urls)),

]
