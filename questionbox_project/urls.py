from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from stackunderflow import views

router = routers.DefaultRouter()
router.register(r'api/questions', views.QuestionsViewSet)
router.register(r'api/answers', views.AnswersViewSet)
router.register(r'api/keywords', views.KeywordViewSet)

app_name = 'stackunderflow'

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^account/logout/$', views.log_out, name='logout'),
    url(r'^account/create/$', views.create_account, name='create_account'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionsPageView.as_view(), name='question_view'),
    url(r'^account/profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
