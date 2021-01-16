from django.db import models

#Basically a project. Allows several 'novels' set in one world.

name_length = 500
description_length = 2000
notes_all = models.TextField(default='')

class World(models.Model):
    name = models.CharField(max_length=name_length)
    description = models.CharField(max_length=description_length)
    notes = notes_all

    def __str__(self):
        return self.name

    """def search_ngi(self):
        ngi = NarrativeGeneralInfo.objects.filter(world=self.id)
        return ngi"""

    def search_general(self,Target):

        search = Target.objects.filter(world=self.id)
        return search

#An individual Narrative, i.e. a single novel, within the World.
class NarrativeGeneralInfo(models.Model):
    title = models.CharField(max_length=name_length,default='')
    description = models.CharField(max_length=description_length,default='')
    notes = notes_all

    setting = models.CharField(max_length=2000)
    genre = models.CharField(max_length=200)
    world = models.ForeignKey(World,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=name_length,default='')
    description = models.CharField(max_length=description_length,default='')
    notes = notes_all
    ngi = models.ForeignKey(NarrativeGeneralInfo,on_delete=models.CASCADE)

    chapter_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Scene(models.Model):
    description = models.CharField(max_length=description_length, default='')
    notes = notes_all
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)
    ngi = models.ForeignKey(NarrativeGeneralInfo, on_delete=models.CASCADE)

    time_and_or_date = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Character(models.Model):
    name = models.CharField(max_length=name_length, default='')
    description = models.CharField(max_length=description_length, default='')
    notes = notes_all

    scenes = models.ManyToManyField(Scene)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=30)
    motive = models.CharField(max_length=50)

    acquaintances = models.ManyToManyField('self',related_name='persons_known')

    def __str__(self):
        return  self.name

class Location(models.Model):
    name = models.CharField(max_length=name_length, default='')
    description = models.CharField(max_length=description_length, default='')
    notes = notes_all
    scenes = models.ManyToManyField(Scene)
    chapters = models.ManyToManyField(Chapter)

    def __str__(self):
        return self.name
