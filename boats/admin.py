from django.contrib import admin

from boats.models.boat import Boat
from boats.models.boat_history import BoatHistory
from boats.models.owner import Owner


# Register your models here.

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'owner',)
    list_filter = ('owner',)


@admin.register(Owner)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(BoatHistory)
class BoatHistoryAdmin(admin.ModelAdmin):
    list_display = ('boat', 'start_year', 'stop_year', 'owner',)
    list_filter = ('boat', 'owner',)



