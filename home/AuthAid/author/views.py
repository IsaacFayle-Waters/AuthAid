from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import World
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'author/index.html'
    context_object_name = 'world_list'
    def get_queryset(self):
        return World.objects.order_by('name')