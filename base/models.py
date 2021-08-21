from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="team/")
    role = models.CharField(max_length=200)
    linkedin = models.URLField(blank=True,null=True)
    github = models.URLField(blank=True,null=True)
    facebook = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    role = models.CharField(choices=(("Star","Star"),("SuperStar","SuperStar"),("Admin","Admin"),("Megastar","Megastar")),max_length=20)


class BuildProject(models.Model):
    name = models.CharField(max_length=200)
    rank = models.IntegerField()

class ActivityWinner(models.Model):
    name = models.CharField(max_length=200)
    rank = models.IntegerField()
    activity = models.CharField(max_length=200)

class StarOfTheWeek(models.Model):
    photo = models.ImageField(upload_to='star/')
    name = models.CharField(max_length=200,default='')
    testimonial = models.TextField(max_length=2048)


class Event(models.Model):
    active = models.BooleanField()
    name = models.CharField(max_length=200)
    rsvp = models.URLField()
    description = models.CharField(max_length=2048)
    image = models.ImageField(upload_to="event/",null=True)