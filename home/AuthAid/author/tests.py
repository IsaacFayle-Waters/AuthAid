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

    def test_text_fields(self):
        world_name = World.objects.create(name='TestWorld',)

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
    #Add two scenes to character, Search to confirm they are there, confirm by comparing the results of the search
    #To the instance defined here
    def test_character_in_scenes_chapters_and_world(self):
        scene_1 = Scene.objects.create(description='Description Test one')
        scene_2 = Scene.objects.create(description='Description Test Two')
        chapter_1 = Chapter.objects.create(title='Title Test One')
        chapter_2 = Chapter.objects.create(title='Title Test Two')
        world_1 = World.objects.create(name='Name Test One World')

        char_1 = Character.objects.create(name='Barry', world=world_1)

        char_1.scenes.add(scene_1,scene_2)
        char_1.chapters.add(chapter_1, chapter_2)

        id_tuple_scene = (scene_1,scene_2)
        id_tuple_chapter = (chapter_1, chapter_2)

        char_1_instance = Character.objects.filter(name='Barry')

        search_ass_result_scene = search_ass(Character,scenes__in=id_tuple_scene).distinct()
        search_ass_result_chapter = search_ass(Character, chapters__in=id_tuple_chapter).distinct()
        search_ass_result_world = search_ass(Character, world=world_1.id)

        self.assertQuerysetEqual(char_1_instance,map(repr,search_ass_result_scene))
        self.assertQuerysetEqual(char_1_instance, map(repr, search_ass_result_chapter))
        self.assertQuerysetEqual(char_1_instance,map(repr,search_ass_result_world))

    # Example: char_1.acquaintances.add(char_3)
    #Ensure characters are added to other charaters acquaintances, and make sure we are not simply comparing 'types'
    #i.e. list(foo) == list(bar) = True
    def test_character_to_character_relationship(self):
        char_1 = Character.objects.create(name="Peanut")
        char_2 = Character.objects.create(name="Romombo")
        char_3 = Character.objects.create(name="Borromidski")

        name_tuple = ("Romombo", "Borromidski")
        name_tuple_wrong = ("Borromidski")

        char_1.acquaintances.add(char_2,char_3)
        char_2.acquaintances.add(char_1)

        char_1_knows_who = Character.objects.filter(name__in=name_tuple)
        char_2_knows_who = Character.objects.filter(name__in=name_tuple_wrong)

        char_1_known = char_1.acquaintances.all()
        char_2_known = char_2.acquaintances.all()

        self.assertEqual(list(char_1_known), list(char_1_knows_who))
        self.assertNotEqual(list(char_2_known), list(char_2_knows_who))


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