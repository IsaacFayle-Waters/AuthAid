from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    #General/initial views
    path('',views.IndexView.as_view(), name='index'),
    path('world/',views.WorldView.as_view(), name='world'),
    path('narrativegeneralinfo/',views.NarrativeGeneralInfoView.as_view(), name='narrativegeneralinfo'),
    path('chapter/',views.ChapterView.as_view(), name='chapter'),
    path('scene/',views.SceneView.as_view(), name='scene'),
    path('character/',views.CharacterView.as_view(), name='character'),
    path('location/',views.LocationView.as_view(),name='location'),

    #Detail Views
    path('world/<int:pk>/',views.WorldDetailView.as_view(),name='world_detail'),
    path('narrativegeneralinfo/<int:pk>/',views.NarrativeGeneralInfoDetailView.as_view(),name='narrative_detail'),
    path('chapter/<int:pk>/',views.ChapterDetailView.as_view(),name='chapter_detail'),
    path('scene/<int:pk>/',views.SceneDetailView.as_view(),name='scene_detail'),
    path('character/<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('location/<int:pk>/', views.LocationDetailView.as_view(), name='location_detail'),

    #Create Views
    path('world_create/',views.WorldCreateView.as_view(),name='world_create'),
    path('narrative_create/',views.NarrativeGeneralInfoCreateView.as_view(),name='narrative_create'),
    path('chapter_create/',views.ChapterCreateView.as_view(),name='chapter_create'),
    path('scene_create/', views.SceneCreateView.as_view(), name='scene_create'),
    path('character_create/', views.CharacterCreateView.as_view(), name='character_create'),
    path('location_create/', views.LocationCreateView.as_view(), name='location_create'),
    #Update Views
    path('world/<int:pk>',views.WorldUpdateView.as_view(),name='world_update'),
    path('narrativegeneralinfo/<int:pk>',views.NarrativeGeneralInfoUpdateView.as_view(),name='narrative_update'),
    path('chapter/<int:pk>',views.ChapterUpdateView.as_view(),name='chapter_update'),
    path('scene/<int:pk>',views.SceneUpdateView.as_view(),name='scene_update'),
    path('character/<int:pk>',views.CharacterUpdateView.as_view(),name='character_update'),
    path('location/<int:pk>',views.LocationUpdateView.as_view(),name='location_update'),
    #Delete Views
    path('world_delete/<int:pk>',views.WorldDeleteView.as_view(),name='world_delete'),
    path('narrative_delete/<int:pk>',views.NarrativeGeneralInfoDeleteView.as_view(),name='narrative_delete'),
    path('chapter_delete/<int:pk>',views.ChapterDeleteView.as_view(),name='chapter_delete'),
    path('scene_delete/<int:pk>', views.SceneDeleteView.as_view(), name='scene_delete'),
    path('character_delete/<int:pk>', views.CharacterDeleteView.as_view(), name='character_delete'),
    path('location_delete/<int:pk>', views.LocationDeleteView.as_view(), name='location_delete'),
]