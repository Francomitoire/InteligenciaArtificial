from django.conf.urls import url
from src import views

urlpatterns = [
    url(r'^classrooms/$', views.classroom_list),
    url(r'^classrooms/(?P<pk>[0-9]+)/$', views.classroom_detail),
]