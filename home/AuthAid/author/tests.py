from django.test import TestCase
from .models import *
from django.utils import timezone
from django.urls import reverse


# Create your tests here.
class WorldModelTests(TestCase):
    def test_name_works_or_not(self):
        world_name = World.objects.create(name='TestWorld')
        self.assertEqual(world_name.name,'TestWorld')
        self.assertNotEqual(world_name.name,'NotTestWorld')

class NarrativeGeneralInfoTests(TestCase):
    def test_title_works_or_not(self):
        ngi_title = NarrativeGeneralInfo.objects.create(title='TestNgi')
        self.assertEqual(ngi_title.title,'TestNgi')
        self.assertNotEqual(ngi_title.title,'NotTestTestNgi')

class ChapterTests(TestCase):
    def test_title_works_or_not(self):
        chapter_title = Chapter.objects.create(title='TestChapter')
        self.assertEqual(chapter_title.title,'TestChapter')
        self.assertNotEqual(chapter_title.title,'NotTestTestChapter')

class SceneTests(TestCase):
    def test_description_works_or_not(self):
        scene_description = Scene.objects.create(description='Everything gets burnt')
        self.assertEqual(scene_description.description,'Everything gets burnt')
        self.assertNotEqual(scene_description.description,'Everything gets repaired')

class CharacterTests(TestCase):
    def test_name_works_or_not(self):
        character_name = Character.objects.create(name='TestMan')
        self.assertEqual(character_name.name,'TestMan')
        self.assertNotEqual(character_name.name,'NotTestMan')

class LocationTests(TestCase):
    def test_name_works_or_not(self):
        location_name = Location.objects.create(name='TestPlace')
        self.assertEqual(location_name.name,'TestPlace')
        self.assertNotEqual(location_name.name,'NotTestPlace')