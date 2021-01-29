from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location, search_ass

'''Helper Functions'''
#Redirect after create,update,delete
def getSuccessUrl():
    return '/author/world'
#Include path form app
def getPathFrom(htmlString):
    return 'author/' + htmlString
#Include path from app, and help with contect object of list type
def getPathFromAndContext_list(htmlString, contextString):
    return 'author/'+ htmlString +'.html', contextString + '_list'
#Get model and template
def getModelTemplate(ModelClass,templateString):
    return ModelClass, getPathFrom(templateString) + '.html'

'''Template Views'''
class IndexView(TemplateView):
    template_name = getPathFrom('index.html')

'''List Views'''
class WorldView(ListView):
    template_name,context_object_name = getPathFromAndContext_list('world', 'world')
    def get_queryset(self):
        return World.objects.all().order_by('name')

class NarrativeGeneralInfoView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('narrativegeneralinfo', 'ngi')
    def get_queryset(self):
        return NarrativeGeneralInfo.objects.all().order_by('world')

class ChapterView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('chapter', 'chapter')
    def get_queryset(self):
        return Chapter.objects.all().order_by('world')

class SceneView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('scene', 'scene')
    def get_queryset(self):
        return Scene.objects.all().order_by('world')

class CharacterView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('character', 'character')
    def get_queryset(self):
        return Character.objects.all().order_by('world')

class LocationView(ListView):
    template_name, context_object_name = getPathFromAndContext_list('location', 'location')
    def get_queryset(self):
        return Location.objects.all().order_by('world')

'''World Views: Detail, Update , Create, Delete '''
class WorldDetailView(DetailView):
    model,template_name = getModelTemplate(World,'world_detail')

class WorldCreateView(CreateView):
    model, template_name = getModelTemplate(World, 'world_create')
    fields = '__all__'
    success_url = getSuccessUrl()

class WorldUpdateView(UpdateView):
    model, template_name = getModelTemplate(World, 'world_update')
    fields = '__all__'
    success_url = getSuccessUrl()

class WorldDeleteView(DeleteView):
    model = World
    success_url = getSuccessUrl()

'''NarrativeGeneralInfo Views:Detail,Create,Update,Delete'''
class NarrativeGeneralInfoDetailView(DetailView):
    model,template_name = getModelTemplate(NarrativeGeneralInfo,'narrative_detail')
    context_object_name = 'ngi'

class NarrativeGeneralInfoCreateView(CreateView):
    model, template_name = getModelTemplate(NarrativeGeneralInfo, 'narrative_create')
    fields = '__all__'
    success_url = getSuccessUrl()

class NarrativeGeneralInfoUpdateView(UpdateView):
    model, template_name = getModelTemplate(NarrativeGeneralInfo, 'narrative_update')
    fields = '__all__'
    success_url = getSuccessUrl()

class NarrativeGeneralInfoDeleteView(DeleteView):
    model = NarrativeGeneralInfo
    success_url = getSuccessUrl()
    context_object_name = 'ngi'

'''Chapter views: Detail, Create, Update, Delete'''
class ChapterDetailView(DetailView):
    model, template_name = getModelTemplate(Chapter, 'chapter_detail')

class ChapterCreateView(CreateView):
    model,template_name = getModelTemplate(Chapter,'chapter_create')
    fields = '__all__'
    success_url = getSuccessUrl()

class ChapterUpdateView(UpdateView):
    model, template_name = getModelTemplate(Chapter, 'chapter_update')
    fields = '__all__'
    success_url = getSuccessUrl()

class ChapterDeleteView(DeleteView):
    model = Chapter
    success_url = getSuccessUrl()

'''Scene views'''
class SceneDetailView(DetailView):
    model, template_name = getModelTemplate(Scene, 'scene_detail')

class SceneCreateView(CreateView):
    model, template_name = getModelTemplate(Scene, 'scene_create')
    fields = '__all__'
    success_url = getSuccessUrl()

class SceneUpdateView(UpdateView):
    model, template_name = getModelTemplate(Scene, 'scene_update')
    fields = '__all__'
    success_url = getSuccessUrl()

class SceneDeleteView(DeleteView):
    model = Scene
    success_url = getSuccessUrl()

'''Character views'''
class CharacterDetailView(DetailView):
    model, template_name = getModelTemplate(Character, 'character_detail')


class CharacterCreateView(CreateView):
    model, template_name = getModelTemplate(Character, 'character_create')
    fields = '__all__'
    success_url = getSuccessUrl()

class CharacterUpdateView(UpdateView):
    model, template_name = getModelTemplate(Character, 'character_update')
    fields = '__all__'
    success_url = getSuccessUrl()

class CharacterDeleteView(DeleteView):
    model = Character
    success_url = getSuccessUrl()

'''Location views'''
class LocationDetailView(DetailView):
    model, template_name = getModelTemplate(Location, 'location_detail')

class LocationCreateView(CreateView):
    model, template_name = getModelTemplate(Location, 'location_create')
    fields = '__all__'
    success_url = getSuccessUrl()

class LocationUpdateView(UpdateView):
    model, template_name = getModelTemplate(Location, 'location_update')
    fields = '__all__'
    success_url = getSuccessUrl()

class LocationDeleteView(DeleteView):
    model = Location
    success_url = getSuccessUrl()