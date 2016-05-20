from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from stackunderflow import views

router = routers.DefaultRouter()
router.register(r'api/questions', views.QuestionsViewSet)
router.register(r'api/answers', views.AnswersViewSet)
# router.register(r'account/create/$', views.CreateAccountView)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^home/$', views.HomeView.as_view()),
    # url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionDetailView.as_view()),
    url(r'^account/create/$', views.CreateAccountView.as_view(), name='create_account'),
    # url(r'^account/profile/(?P<pk>[0-9]+)/$', views.ProfileView.as_view()),
    url(r'^admin/', include(admin.site.urls)),

]
