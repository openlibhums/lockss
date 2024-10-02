from django.urls import re_path

from plugins.clockss import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]
