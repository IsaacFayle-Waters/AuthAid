from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView,DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location, search_ass
from .forms import NgiForm, ChapterForm, SceneForm, CharacterForm, LocationForm
from .customFields import *

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
class IndexView(LoginRequiredMixin,TemplateView):
    template_name = getPathFrom('index.html')
    login_url = '../core'

'''List Views'''
class WorldView(LoginRequiredMixin,ListView):
    template_name,context_object_name = getPathFromAndContext_list('world', 'world')
    login_url = '../../core'
    def get_queryset(self):
        return World.objects.all().filter(user=self.request.user)

class NarrativeGeneralInfoView(LoginRequiredMixin,ListView):
    template_name, context_object_name = getPathFromAndContext_list('narrativegeneralinfo', 'ngi')
    login_url = '../../core'
    def get_queryset(self):
        return NarrativeGeneralInfo.objects.all().filter(user=self.request.user)

class ChapterView(LoginRequiredMixin,ListView):
    template_name, context_object_name = getPathFromAndContext_list('chapter', 'chapter')
    login_url = '../../core'
    def get_queryset(self):
        return Chapter.objects.all().filter(user=self.request.user)

class SceneView(LoginRequiredMixin,ListView):
    template_name, context_object_name = getPathFromAndContext_list('scene', 'scene')
    login_url = '../../core'
    def get_queryset(self):
        return Scene.objects.all().filter(user=self.request.user)

class CharacterView(LoginRequiredMixin,ListView):
    template_name, context_object_name = getPathFromAndContext_list('character', 'character')
    login_url = '../../core'
    def get_queryset(self):
        return Character.objects.all().filter(user=self.request.user)

class LocationView(LoginRequiredMixin,ListView):
    template_name, context_object_name = getPathFromAndContext_list('location', 'location')
    login_url = '../../core'
    def get_queryset(self):
        return Location.objects.all().filter(user=self.request.user)

'''World Views: Detail, Update , Create, Delete '''
class WorldDetailView(LoginRequiredMixin,DetailView):
    model,template_name = getModelTemplate(World,'world_detail')

class WorldCreateView(LoginRequiredMixin,CreateView):
    model, template_name = getModelTemplate(World, 'world_create')
    fields = worldFields
    success_url = getSuccessUrl()
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(WorldCreateView,self).form_valid(form)

class WorldUpdateView(LoginRequiredMixin,UpdateView):
    model, template_name = getModelTemplate(World, 'world_update')
    fields = worldFields
    success_url = getSuccessUrl()

class WorldDeleteView(LoginRequiredMixin,DeleteView):
    model = World
    success_url = getSuccessUrl()

'''NarrativeGeneralInfo Views:Detail,Create,Update,Delete'''
class NarrativeGeneralInfoDetailView(LoginRequiredMixin,DetailView):
    model,template_name = getModelTemplate(NarrativeGeneralInfo,'narrative_detail')
    context_object_name = 'ngi'

class NarrativeGeneralInfoCreateView(LoginRequiredMixin,CreateView):
    model, template_name = getModelTemplate(NarrativeGeneralInfo, 'narrative_create')
    form_class = NgiForm
    success_url = getSuccessUrl()

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(NarrativeGeneralInfoCreateView,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(NarrativeGeneralInfoCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class NarrativeGeneralInfoUpdateView(LoginRequiredMixin,UpdateView):
    model, template_name = getModelTemplate(NarrativeGeneralInfo, 'narrative_update')
    form_class = NgiForm
    success_url = getSuccessUrl()

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(NarrativeGeneralInfoUpdateView,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(NarrativeGeneralInfoUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class NarrativeGeneralInfoDeleteView(LoginRequiredMixin,DeleteView):
    model = NarrativeGeneralInfo
    success_url = getSuccessUrl()
    context_object_name = 'ngi'

'''Chapter views: Detail, Create, Update, Delete'''
class ChapterDetailView(LoginRequiredMixin,DetailView):
    model, template_name = getModelTemplate(Chapter, 'chapter_detail')

class ChapterCreateView(LoginRequiredMixin,CreateView):
    model,template_name = getModelTemplate(Chapter,'chapter_create')
    form_class = ChapterForm
    success_url = getSuccessUrl()

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(ChapterCreateView,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ChapterCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ChapterUpdateView(LoginRequiredMixin,UpdateView):
    model, template_name = getModelTemplate(Chapter, 'chapter_update')
    form_class = ChapterForm
    success_url = getSuccessUrl()
    '''
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(ChapterUpdateView,self).form_valid(form)
    '''
    def get_form_kwargs(self):
        kwargs = super(ChapterUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ChapterDeleteView(LoginRequiredMixin,DeleteView):
    model = Chapter
    success_url = getSuccessUrl()

'''Scene views'''
class SceneDetailView(LoginRequiredMixin,DetailView):
    model, template_name = getModelTemplate(Scene, 'scene_detail')

class SceneCreateView(LoginRequiredMixin,CreateView):
    model, template_name = getModelTemplate(Scene, 'scene_create')
    form_class = SceneForm
    success_url = getSuccessUrl()

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(SceneCreateView,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(SceneCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class SceneUpdateView(LoginRequiredMixin,UpdateView):
    model, template_name = getModelTemplate(Scene, 'scene_update')
    form_class = SceneForm
    success_url = getSuccessUrl()

    def get_form_kwargs(self):
        kwargs = super(SceneUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class SceneDeleteView(LoginRequiredMixin,DeleteView):
    model = Scene
    success_url = getSuccessUrl()

'''Character views'''
class CharacterDetailView(LoginRequiredMixin,DetailView):
    model, template_name = getModelTemplate(Character, 'character_detail')

class CharacterCreateView(LoginRequiredMixin,CreateView):
    model, template_name = getModelTemplate(Character, 'character_create')
    form_class = CharacterForm
    success_url = getSuccessUrl()

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(CharacterCreateView,self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CharacterCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CharacterUpdateView(LoginRequiredMixin,UpdateView):
    model, template_name = getModelTemplate(Character, 'character_update')
    form_class = CharacterForm
    success_url = getSuccessUrl()

    def get_form_kwargs(self):
        kwargs = super(CharacterUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CharacterDeleteView(LoginRequiredMixin,DeleteView):
    model = Character
    success_url = getSuccessUrl()

'''Location views'''
class LocationDetailView(LoginRequiredMixin,DetailView):
    model, template_name = getModelTemplate(Location, 'location_detail')

class LocationCreateView(LoginRequiredMixin,CreateView):
    model, template_name = getModelTemplate(Location, 'location_create')
    form_class = LocationForm
    success_url = getSuccessUrl()

    def get_form_kwargs(self):
        kwargs = super(LocationCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(LocationCreateView,self).form_valid(form)

class LocationUpdateView(LoginRequiredMixin,UpdateView):
    model, template_name = getModelTemplate(Location, 'location_update')
    form_class = LocationForm
    success_url = getSuccessUrl()

    def get_form_kwargs(self):
        kwargs = super(LocationUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class LocationDeleteView(LoginRequiredMixin,DeleteView):
    model = Location
    success_url = getSuccessUrl()