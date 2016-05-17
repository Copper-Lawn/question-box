from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from stackunderflow import views

router = routers.DefaultRouter()
router.register(r'api/questions', views.QuestionsViewSet)
router.register(r'api/answers', views.AnswersViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),

]
