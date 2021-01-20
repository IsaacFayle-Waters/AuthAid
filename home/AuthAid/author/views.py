from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location, search_ass
# Create your views here.

class IndexView(TemplateView):
    template_name = 'author/index.html'
    context_object_name = 'world_list'

class WorldView(ListView):
    template_name = 'author/world.html'
    context_object_name = 'world_list'
    def get_queryset(self):
        return World.objects.all()

class NarrativeGeneralInfoView(ListView):
    template_name = 'author/narrativegeneralinfo.html'
    context_object_name = 'ngi_list'
    def get_queryset(self):
        return NarrativeGeneralInfo.objects.all()

class ChapterView(ListView):
    template_name = 'author/chapter.html'

class SceneView(ListView):
    template_name = 'author/scene.html'

class CharacterView(ListView):
    template_name = 'author/character.html'

class LocationView(ListView):
    template_name = 'author/location.html'