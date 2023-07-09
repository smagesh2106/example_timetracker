from django.db import models
from account.models import CustomUser


# Team has many engineers, but an engineer can belong to only one team
class Team( models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    member = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

# Project as many engineers, an engineer can belore to many projects
class Project( models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255)
    members = models.ManyToManyField(CustomUser)

class TimeSheet( models.Model):
    summary = models.TextField(max_length=255)
    location = models.CharField(max_length=25)
    date = models.DateField()
    startime = models.TimeField()
    endtime = models.TimeField()
    login = models.DateTimeField()
    logout = models.DateTimeField()
    staff = models.ManyToManyField(CustomUser )
