from django.db import models
from django.urls import reverse
#These don't work with sqlite3?
name_length = 500
description_length = 2000
notes_all = models.TextField(default='',blank=True)

"""Search for assignments of an instance of a class in instances of other classes.
#EXAMPLE OF USAGE:
    #w = World.objects.get(pk=1)
    #search_ass(NarrativeGeneralInfo,world=w.id)
"""
def search_ass(Target, **kwargs):
    return Target.objects.filter(**kwargs)

#Basically a project. Allows several 'novels'(ngi's) set in one world/universe.
class World(models.Model):
    name = models.CharField(max_length=name_length, default='',blank=True)
    description = models.CharField(max_length=description_length, default='',blank=True)
    notes = notes_all

    def __str__(self):
        return self.name

#An individual Narrative, i.e. a single novel, within the World.
class NarrativeGeneralInfo(models.Model):
    title = models.CharField(max_length=name_length,default='',blank=True)
    description = models.CharField(max_length=description_length,default='',blank=True)
    notes = notes_all

    setting = models.CharField(max_length=2000, default='',blank=True)
    genre = models.CharField(max_length=200, default='',blank=True)
    world = models.ForeignKey(World,on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=name_length,default='',blank=True)
    description = models.CharField(max_length=description_length,default='',blank=True)
    notes = notes_all
    ngi = models.ForeignKey(NarrativeGeneralInfo,on_delete=models.CASCADE, null=True,blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, null=True,blank=True)
    #TODO: DECIDE HOW TO HANDLE CHAPTER NUMBERS
    chapter_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Scene(models.Model):
    description = models.CharField(max_length=description_length, default='',blank=True)
    notes = notes_all
    time_and_or_date = models.CharField(max_length=100, default='',blank=True)

    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE, null=True,blank=True)
    ngi = models.ForeignKey(NarrativeGeneralInfo, on_delete=models.CASCADE, null=True,blank=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.description

class Character(models.Model):
    name = models.CharField(max_length=name_length, default='',blank=True)
    surname = models.CharField(max_length=name_length, default='',blank=True)
    description = models.CharField(max_length=description_length, default='',blank=True)
    notes = notes_all
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=30, default='',blank=True)
    motive = models.CharField(max_length=50, default='',blank=True)

    world = models.ForeignKey(World, on_delete=models.CASCADE, null=True,blank=True)
    #TODO: Make sure many to many class works and is actually appropriate.
    scenes = models.ManyToManyField(Scene,blank=True)
    chapters = models.ManyToManyField(Chapter,blank=True)

    #Basic relationships between characters, in this case whether they know each other
    #c1.acquaintances.add(c2)
    acquaintances = models.ManyToManyField('self',related_name='persons_known',blank=True)

    def __str__(self):
        return  self.name

class Location(models.Model):
    name = models.CharField(max_length=name_length, default='',blank=True)
    description = models.CharField(max_length=description_length, default='',blank=True)
    notes = notes_all

    world = models.ForeignKey(World, on_delete=models.CASCADE, null=True,blank=True)
    scenes = models.ManyToManyField(Scene,blank=True)
    chapters = models.ManyToManyField(Chapter,blank=True)

    def __str__(self):
        return self.name
