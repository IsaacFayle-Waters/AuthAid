from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location, search_ass

class IndexView(TemplateView):
    template_name = 'author/index.html'

'''List Views'''
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

'''World Views: Detail, Update , Create, Delete '''
class WorldDetailView(DetailView):
    model = World
    template_name = 'author/world_detail.html'

class WorldUpdateView(UpdateView):
    model = World
    fields = '__all__'
    template_name = 'author/world_update.html'
    success_url = '/author/world'

class WorldCreateView(CreateView):
    model = World
    fields = '__all__'
    template_name = 'author/world_create.html'
    success_url = '/author/world'

class WorldDeleteView(DeleteView):
    model = World
    success_url = '/author/world'

'''NarrativeGeneralInfo Views'''
class NarrativeGeneralInfoDetailView(DetailView):
    model = NarrativeGeneralInfo
    template_name = 'author/narrative_detail.html'
    context_object_name = 'ngi'

'''Chapter views'''
class ChapterDetailView(DetailView):
    model = Chapter
    template_name = 'author/chapter_detail.html'

'''Scene views'''
class SceneDetailView(DetailView):
    model = Scene
    template_name = 'author/scene_detail.html'

'''Character views'''
class CharacterDetailView(DetailView):
    model = Character
    template_name = 'author/character_detail.html'

'''Location views'''
class LocationDetailView(DetailView):
    model = Location
    template_name = 'author/location_detail.html'