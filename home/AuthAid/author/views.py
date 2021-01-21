from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView
from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location, search_ass
# Create your views here.

class IndexView(TemplateView):
    template_name = 'author/index.html'
    context_object_name = 'world_list'

class WorldView(ListView):
    template_name = 'author/world.html'
    context_object_name = 'world_list'
    def get_queryset(self):
        return World.objects.all().order_by('name')

class NarrativeGeneralInfoView(ListView):
    template_name = 'author/narrativegeneralinfo.html'
    context_object_name = 'ngi_list'
    def get_queryset(self):
        return NarrativeGeneralInfo.objects.all().order_by('world')

class ChapterView(ListView):
    template_name = 'author/chapter.html'
    context_object_name = 'chapter_list'
    def get_queryset(self):
        return Chapter.objects.all().order_by('world')

class SceneView(ListView):
    template_name = 'author/scene.html'
    context_object_name = 'scene_list'
    def get_queryset(self):
        return Scene.objects.all().order_by('world')

class CharacterView(ListView):
    template_name = 'author/character.html'
    context_object_name = 'character_list'
    def get_queryset(self):
        return Character.objects.all().order_by('world')

class LocationView(ListView):
    template_name = 'author/location.html'
    context_object_name = 'location_list'

    def get_queryset(self):
        return Location.objects.all().order_by('world')

