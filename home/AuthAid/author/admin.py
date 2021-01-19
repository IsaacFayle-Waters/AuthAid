from django.contrib import admin
from .models import World, NarrativeGeneralInfo, Chapter, Scene, Character, Location
# Register your models here.


admin.site.register(World)
admin.site.register(NarrativeGeneralInfo)
admin.site.register(Chapter)
admin.site.register(Scene)
admin.site.register(Character)
admin.site.register(Location)