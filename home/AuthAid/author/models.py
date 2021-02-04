from django.db import models
from django.conf import settings
#These don't work with sqlite3?
name_length = 500
description_length = 2000
notes_all = models.TextField(default='',blank=True)


#Search for assignments of an instance of a class in instances of other classes.
#EXAMPLE OF USAGE:#w = World.objects.get(pk=1), #search_ass(NarrativeGeneralInfo,world=w.id)
def search_ass(Target, **kwargs):
    return Target.objects.filter(**kwargs)

'''Helper functions'''
#Basic input Fields
def charFieldsAndNotes():
    nameTitle =  models.CharField(max_length=name_length, default='',blank=True)
    description = models.CharField(max_length=description_length, default='',blank=True)
    notes = notes_all
    return nameTitle,description,notes
#Return a foreign key with on_delete set to null. i.e. don't remove conected instances
def setForeignKeysNullDelete(TargetClass):
    return models.ForeignKey(TargetClass,on_delete=models.SET_NULL, null=True,blank=True)
#Return a foriegnkey that when deleted deletes conected instances.
def setForeignKeysCascadeDelete(TargetClass):
    return models.ForeignKey(TargetClass,on_delete=models.CASCADE, null=True,blank=True)

'''The Models'''
#Basically a project. Allows several 'novels'(ngi's) set in one world/universe.
class World(models.Model):
    name,description,notes = charFieldsAndNotes()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='world', null=True)

    def __str__(self):
        return self.name

    def ngis(self):
        return search_ass(NarrativeGeneralInfo, world=self)

    def chapters(self):
        return search_ass(Chapter, world=self)

    def scenes(self):
        return search_ass(Scene, world=self)

    def characters(self):
        return search_ass(Character,world=self)

    def locations(self):
        return search_ass(Location,world=self)

#An individual Narrative, i.e. a single novel, within the World.
class NarrativeGeneralInfo(models.Model):
    title,description,notes = charFieldsAndNotes()
    setting = models.CharField(max_length=2000, default='',blank=True)
    genre = models.CharField(max_length=200, default='',blank=True)
    world = setForeignKeysCascadeDelete(World)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='narrativegeneralinfo', null=True)
    def __str__(self):
        return self.title

    def chapters(self):
        return search_ass(Chapter,ngi=self)

    def scenes(self):
        return search_ass(Scene,ngi=self)

    def characters(self):
        return search_ass(Character,ngi=self)

    def locations(self):
        return search_ass(Location,ngi=self)

class Chapter(models.Model):
    title, description, notes = charFieldsAndNotes()
    ngi = setForeignKeysNullDelete(NarrativeGeneralInfo)
    world = setForeignKeysCascadeDelete(World)
    #TODO: DECIDE HOW TO HANDLE CHAPTER NUMBERS
    chapter_number = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chapter', null=True)

    def __str__(self):
        return self.title

    def scenes(self):
        return search_ass(Scene,chapter=self)

    def characters(self):
        return search_ass(Character,chapters=self)

    def locations(self):
        return search_ass(Location,chapters=self)

class Scene(models.Model):

    description = models.CharField(max_length=description_length, default='',blank=True)
    notes = notes_all
    time_and_or_date = models.CharField(max_length=100, default='',blank=True)

    chapter = setForeignKeysNullDelete(Chapter)
    ngi = setForeignKeysNullDelete(NarrativeGeneralInfo)
    world = setForeignKeysCascadeDelete(World)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='scene', null=True)
    def __str__(self):
        return self.description

    def characters(self):
        return search_ass(Character,scenes=self)

    def locations(self):
        return search_ass(Location,scenes=self)

class Character(models.Model):
    name,description,notes = charFieldsAndNotes()
    surname = models.CharField(max_length=name_length, default='',blank=True)
    #TODO: age can expeirence OverflowError if figure too high
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=30, default='',blank=True)
    motive = models.CharField(max_length=50, default='',blank=True)

    #Don't completley delete Character if World Deletes, incase Character to be used elsewhere
    world = setForeignKeysNullDelete(World)
    scenes = models.ManyToManyField(Scene,blank=True)
    chapters = models.ManyToManyField(Chapter,blank=True)
    ngi = models.ManyToManyField(NarrativeGeneralInfo,blank=True)

    #Basic relationships between characters, in this case whether they know each other
    #c1.acquaintances.add(c2)
    acquaintances = models.ManyToManyField('self',related_name='persons_known',blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='character', null=True)
    def __str__(self):
        return  self.name

class Location(models.Model):
    name, description, notes = charFieldsAndNotes()
    world = world = setForeignKeysNullDelete(World)
    ngi = models.ManyToManyField(NarrativeGeneralInfo)
    scenes = models.ManyToManyField(Scene,blank=True)
    chapters = models.ManyToManyField(Chapter,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='location', null=True)
    def __str__(self):
        return self.name
