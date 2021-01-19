from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('<int:pk>/',views.WorldView.as_view(), name='world'),
    path('',views.NgiView.as_view(), name='ngi'),
    path('',views.ChapterView.as_view(), name='chapter'),
    path('',views.SceneView.as_view(), name='scene'),
    path('',views.CharacterView.as_view(), name='character'),
    path('',views.LocationView.as_view(),name='location')

]