from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [path('',views.IndexView.as_view(),name='index'),


               ]