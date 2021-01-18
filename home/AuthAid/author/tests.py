from django.test import TestCase
from .models import *
from django.utils import timezone
from django.urls import reverse


# Create your tests here.
class WorldModelTests(TestCase):
    def test_name_works_or_not(self):
        world_name = World.objects.create(name='TestWorld')
        self.assertEqual(world_name.__str__(),'TestWorld')
        self.assertNotEqual(world_name.__str__(),'NotTestWorld')

class NarrativeGeneralInfoTests(TestCase):
    def test_title_works_or_not(self):
        ngi_title = NarrativeGeneralInfo.objects.create(title='TestNgi')
        self.assertEqual(ngi_title.__str__(),'TestNgi')
        self.assertNotEqual(ngi_title.__str__(),'NotTestTestNgi')

class ChapterTests(TestCase):
    def test_title_works_or_not(self):
        chapter_title = Chapter.objects.create(title='TestChapter')
        self.assertEqual(chapter_title.__str__(),'TestChapter')
        self.assertNotEqual(chapter_title.__str__(),'NotTestTestChapter')

class SceneTests(TestCase):
    def test_description_works_or_not(self):
        scene_description = Scene.objects.create(description='Everything gets burnt')
        self.assertEqual(scene_description.__str__(),'Everything gets burnt')
        self.assertNotEqual(scene_description.__str__(),'Everything gets repaired')

class CharacterTests(TestCase):
    def test_name_works_or_not(self):
        character_name = Character.objects.create(name='TestMan')
        self.assertEqual(character_name.__str__(),'TestMan')
        self.assertNotEqual(character_name.__str__(),'NotTestMan')

class LocationTests(TestCase):
    def test_name_works_or_not(self):
        location_name = Location.objects.create(name='TestPlace')
        self.assertEqual(location_name.__str__(),'TestPlace')
        self.assertNotEqual(location_name.__str__(),'NotTestPlace')

class NonModelFunctionsTest(TestCase):
    def test_search_ass(self):
        world_instance = World.objects.create(name="TestWorld")
        ngi_instance = NarrativeGeneralInfo.objects.filter(world=world_instance)
        search_ass_result = search_ass(NarrativeGeneralInfo,world = world_instance.id)
        self.assertQuerysetEqual( ngi_instance,search_ass_result)