from django.shortcuts import render
from .models import ActivityWinner, BuildProject, Event, StarOfTheWeek, Team
# Create your views here.
def home(request):
    megastar = Team.objects.filter(role="Megastar")
    admin = Team.objects.filter(role="Admin")
    star = Team.objects.filter(role="Star")
    superstar = Team.objects.filter(role="SuperStar")
    build = BuildProject.objects.all()
    activity = ActivityWinner.objects.all()
    starofweek = StarOfTheWeek.objects.all()
    event = Event.objects.all()
    return render(request,"home.html",{'megastar':megastar,'admin':admin,'star':star,'superstar':superstar,'activity':activity,'build':build,'starofweek':starofweek,'event':event})