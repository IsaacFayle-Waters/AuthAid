from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('^$/world',views.WorldView.as_view(), name='world'),
    path('^$/narrativegeneralinfo/',views.NarrativeGeneralInfoView.as_view(), name='narrativegeneralinfo'),
    path('^$/chapter/',views.ChapterView.as_view(), name='chapter'),
    path('^$/scene/',views.SceneView.as_view(), name='scene'),
    path('^$/character/',views.CharacterView.as_view(), name='character'),
    path('^$/location/',views.LocationView.as_view(),name='location')

]