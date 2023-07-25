

from django.contrib import admin
from django.urls import path, include
from boats.apps import BoatsConfig
from boats.views import BoatListView

app_name = BoatsConfig.name

urlpatterns = [
    path('', BoatListView.as_view(), name='boats_list'),

]