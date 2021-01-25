from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location, search_ass

'''Helper Functions'''
def getSuccessUrl():
    return '/author/world'

def getPathFrom(htmlString):
    return 'author/' + htmlString

def getPathFromAndContext_list(htmlString, contextString):
    return 'author/'+ htmlString, contextString + '_list'

'''Template Views'''
class IndexView(TemplateView):
    template_name = getPathFrom('index.html')

'''List Views'''
class WorldView(ListView):
    template_name,context_object_name = getPathFromAndContext_list('world.html', 'world')
    def get_queryset(self):
        return World.objects.all().order_by('name')

class NarrativeGeneralInfoView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('narrativegeneralinfo.html', 'ngi')
    def get_queryset(self):
        return NarrativeGeneralInfo.objects.all().order_by('world')

class ChapterView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('chapter.html', 'chapter')
    def get_queryset(self):
        return Chapter.objects.all().order_by('world')

class SceneView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('scene.html', 'scene')
    def get_queryset(self):
        return Scene.objects.all().order_by('world')

class CharacterView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('character.html', 'character')
    def get_queryset(self):
        return Character.objects.all().order_by('world')

class LocationView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('location.html', 'location')
    def get_queryset(self):
        return Location.objects.all().order_by('world')

'''World Views: Detail, Update , Create, Delete '''
class WorldDetailView(DetailView):
    model = World
    template_name = getPathFrom('world_detail.html')

class WorldCreateView(CreateView):
    model = World
    fields = '__all__'
    template_name = getPathFrom('world_create.html')
    success_url = getSuccessUrl()

class WorldUpdateView(UpdateView):
    model = World
    fields = '__all__'
    template_name = getPathFrom('world_update.html')
    success_url = getSuccessUrl()

class WorldDeleteView(DeleteView):
    model = World
    success_url = getSuccessUrl()

'''NarrativeGeneralInfo Views:Detail,Create,Update,Delete'''
class NarrativeGeneralInfoDetailView(DetailView):
    model = NarrativeGeneralInfo
    template_name = getPathFrom('narrative_detail.html')
    context_object_name = 'ngi'

class NarrativeGeneralInfoCreateView(CreateView):
     model = NarrativeGeneralInfo
     fields = '__all__'
     template_name = getPathFrom('narrative_create.html')
     success_url = getSuccessUrl()

class NarrativeGeneralInfoUpdateView(UpdateView):
    model = NarrativeGeneralInfo
    fields = '__all__'
    template_name = getPathFrom('narrative_update.html')
    success_url = getSuccessUrl()

class NarrativeGeneralInfoDeleteView(DeleteView):
    model = NarrativeGeneralInfo
    success_url = getSuccessUrl()
    context_object_name = 'ngi'

'''Chapter views: Detail, Create, Update, Delete'''
class ChapterDetailView(DetailView):
    model = Chapter
    template_name = getPathFrom('chapter_detail.html')

class ChapterCreateView(CreateView):
    model = Chapter
    fields = '__all__'
    template_name = getPathFrom('chapter_create.html')
    success_url = getSuccessUrl()

class ChapterUpdateView(UpdateView):
    model = Chapter
    fields = '__all__'
    template_name = getPathFrom('chapter_update.html')
    success_url = getSuccessUrl()

class ChapterDeleteView(DeleteView):
    model = Chapter
    success_url = getSuccessUrl()

'''Scene views'''
class SceneDetailView(DetailView):
    model = Scene
    template_name = getPathFrom('scene_detail.html')

class SceneCreateView(CreateView):
    model = Scene
    fields = '__all__'
    template_name = getPathFrom('scene_create.html')
    success_url = getSuccessUrl()

class SceneUpdateView(UpdateView):
    model = Scene
    fields = '__all__'
    template_name = getPathFrom('scene_update.html')
    success_url = getSuccessUrl()

class SceneDeleteView(DeleteView):
    model = Scene
    success_url = getSuccessUrl()

'''Character views'''
class CharacterDetailView(DetailView):
    model = Character
    template_name = getPathFrom('character_detail.html')

class CharacterCreateView(CreateView):
    model = Character
    fields = '__all__'
    template_name = getPathFrom('character_create.html')
    success_url = getSuccessUrl()

class CharacterUpdateView(UpdateView):
    model = Character
    fields = '__all__'
    template_name = getPathFrom('character_update.html')
    success_url = getSuccessUrl()

class CharacterDeleteView(DeleteView):
    model = Character
    success_url = getSuccessUrl()

'''Location views'''
class LocationDetailView(DetailView):
    model = Location
    template_name = getPathFrom('location_detail.html')

class LocationCreateView(CreateView):
    model = Location
    fields = '__all__'
    template_name = getPathFrom('location_create.html')
    success_url = getSuccessUrl()

class LocationUpdateView(UpdateView):
    model = Location
    fields = '__all__'
    template_name = getPathFrom('location_update.html')
    success_url = getSuccessUrl()

class LocationDeleteView(DeleteView):
    model = Location
    success_url = getSuccessUrl()
