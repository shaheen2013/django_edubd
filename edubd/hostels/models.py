from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import mimetypes
import os

# Create your models here.

#-----------------------hostel type --------------------
class HostelType(models.Model):
    type=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type 





#-----------------------room type --------------------
class RoomType(models.Model):
    type=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type 

#-----------------------room  --------------------
class Room(models.Model):
    number=models.CharField(max_length=200)
    number_of_bed=models.IntegerField(null=True)
    bed_cost=models.FloatField(null=True)
    type=models.ForeignKey(RoomType,null=True, on_delete=models.SET_NULL)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number 


#-----------------------hostel  --------------------
class Hostel(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField(max_length=200, null=True)
    history=models.TextField(max_length=200, null=True,blank=True)
    description=models.TextField(max_length=200, null=True, blank=True)
    type=models.ForeignKey(HostelType,null=True, on_delete=models.SET_NULL)
    room=models.ManyToManyField(Room, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

#-----------------------hostel room staff --------------------
class HostelRoomStudent(models.Model):
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL, unique=True)
    hostel=models.ForeignKey(Hostel,null=True, on_delete=models.SET_NULL, blank=True)
    room=models.ForeignKey(Room,null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)

    """ def __str__(self):
        return self.name """ 

#----------------------- designation--------------------

class Designation(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

#-----------------------assign hostel staff--------------------

class HostelStaff(models.Model):
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    hostel=models.ForeignKey(Hostel,null=True, on_delete=models.SET_NULL, blank=True)
    designation=models.ForeignKey(Designation,null=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)


