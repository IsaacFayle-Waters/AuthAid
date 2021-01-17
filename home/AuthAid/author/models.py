from django.db import models

name_length = 500
description_length = 2000
notes_all = models.TextField(default='')
#Basically a project. Allows several 'novels'(ngi's) set in one world/universe.
class World(models.Model):
    name = models.CharField(max_length=name_length)
    description = models.CharField(max_length=description_length)
    notes = notes_all

    def __str__(self):
        return self.name

    """def search_ngi(self):
        ngi = NarrativeGeneralInfo.objects.filter(world=self.id)
        return ngi"""
    #Search for references to self in instances of other classes, and return list of those instances
    def search_general(self,Target):
            return Target.objects.filter(world=self.id)

#An individual Narrative, i.e. a single novel, within the World.
class NarrativeGeneralInfo(models.Model):
    title = models.CharField(max_length=name_length,default='')
    description = models.CharField(max_length=description_length,default='')
    notes = notes_all

    setting = models.CharField(max_length=2000, default='')
    genre = models.CharField(max_length=200, default='')
    world = models.ForeignKey(World,on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title

        # Search for references to self in instances of other classes, and return list of those instances
    def search_general(self,Target):
        return Target.objects.filter(ngi=self.id)

class Chapter(models.Model):
    title = models.CharField(max_length=name_length,default='')
    description = models.CharField(max_length=description_length,default='')
    notes = notes_all
    ngi = models.ForeignKey(NarrativeGeneralInfo,on_delete=models.CASCADE)
    #TODO: DECIDE HOW TO HANDLE CHAPTER NUMBERS
    chapter_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

        # Search for references to self in instances of other classes, and return list of those instances
    def search_general(self, Target):
        return Target.objects.filter(chapter=self.id)

class Scene(models.Model):
    description = models.CharField(max_length=description_length, default='')
    notes = notes_all
    time_and_or_date = models.CharField(max_length=100, default='')

    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE, default='')
    ngi = models.ForeignKey(NarrativeGeneralInfo, on_delete=models.CASCADE, default='')
    world = models.ForeignKey(World, on_delete=models.CASCADE, default='')


    def __str__(self):
        return self.description

    #NOT TESTED. Not sure if workable with many to many.
    def search_general(self, Target):
        return Target.objects.filter(scene=self.id)

class Character(models.Model):
    name = models.CharField(max_length=name_length, default='')
    description = models.CharField(max_length=description_length, default='')
    notes = notes_all

    world = models.ForeignKey(World, on_delete=models.CASCADE, null=True)
    scenes = models.ManyToManyField(Scene)
    chapters = models.ManyToManyField(Chapter)

    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=30, default='')
    motive = models.CharField(max_length=50, default='')
    #Basic relationships between characters, in this case whether they know each other
    acquaintances = models.ManyToManyField('self',related_name='persons_known')

    def __str__(self):
        return  self.name

class Location(models.Model):
    name = models.CharField(max_length=name_length, default='')
    description = models.CharField(max_length=description_length, default='')
    notes = notes_all

    world = models.ForeignKey(World, on_delete=models.CASCADE, default='')
    scenes = models.ManyToManyField(Scene)
    chapters = models.ManyToManyField(Chapter)

    def __str__(self):
        return self.name
