from django.contrib import admin
from .models import Team,BuildProject,ActivityWinner,StarOfTheWeek,Event
# Register your models here.

class TeamRef(admin.ModelAdmin):
    list_display = ['name','role']
    list_filter = ['role']

admin.site.register(Team,TeamRef)

class BuildProjectRef(admin.ModelAdmin):
    list_display = ['name','rank']

admin.site.register(BuildProject,BuildProjectRef)

class ActivityWinnerRef(admin.ModelAdmin):
    list_display = ['name','rank','activity']

admin.site.register(ActivityWinner,ActivityWinnerRef)

class StarOfTheWeekRef(admin.ModelAdmin):
    list_display = ['name','testimonial']

admin.site.register(StarOfTheWeek,StarOfTheWeekRef)

class EventRef(admin.ModelAdmin):
    list_display = ['name','description']
    list_filter = ['active']

admin.site.register(Event,EventRef)