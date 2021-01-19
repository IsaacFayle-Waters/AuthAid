from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location, search_ass
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'author/index.html'
    context_object_name = 'world_list'
    def get_queryset(self):
        return World.objects.order_by('name')

class WorldView(generic.ListView):
    pass

class NarrativeGeneralInfoView(generic.ListView):
    pass

class ChapterView(generic.ListView):
    pass

class SceneView(generic.ListView):
    pass

class CharacterView(generic.ListView):
    pass

class LocationView(generic.ListView):
    pass