from django.shortcuts import render
from django.views.generic import ListView
from boats.models.boat import Boat
from django.urls import reverse_lazy


# Create your views here.

class BoatListView(ListView):
    model = Boat
    success_url = reverse_lazy('boat:list')