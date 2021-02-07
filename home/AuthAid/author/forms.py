from django.forms import ModelForm
from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location, search_ass
from .customFields import *

class NgiForm(ModelForm):
    class Meta:
        model = NarrativeGeneralInfo
        fields = ngiFields
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super(NgiForm, self).__init__(*args, **kwargs)
        self.fields['world'].queryset = World.objects.filter(user=user)

class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = chapterFields
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super(ChapterForm, self).__init__(*args, **kwargs)
        self.fields['world'].queryset = World.objects.filter(user=user)
        self.fields['ngi'].queryset = NarrativeGeneralInfo.objects.filter(user=user)

class SceneForm(ModelForm):
    class Meta:
        model = Scene
        fields = sceneFields
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super(SceneForm, self).__init__(*args, **kwargs)
        self.fields['world'].queryset = World.objects.filter(user=user)
        self.fields['ngi'].queryset = NarrativeGeneralInfo.objects.filter(user=user)
        self.fields['chapter'].queryset = Chapter.objects.filter(user=user)

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = characterFields
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super(CharacterForm, self).__init__(*args, **kwargs)
        self.fields['world'].queryset = World.objects.filter(user=user)
        self.fields['ngi'].queryset = NarrativeGeneralInfo.objects.filter(user=user)
        self.fields['chapters'].queryset = Chapter.objects.filter(user=user)
        self.fields['scenes'].queryset = Scene.objects.filter(user=user)
        self.fields['acquaintances'].queryset = Character.objects.filter(user=user)

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = locationFields

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super(LocationForm, self).__init__(*args, **kwargs)
        self.fields['world'].queryset = World.objects.filter(user=user)
        self.fields['ngi'].queryset = NarrativeGeneralInfo.objects.filter(user=user)
        self.fields['chapters'].queryset = Chapter.objects.filter(user=user)
        self.fields['scenes'].queryset = Scene.objects.filter(user=user)