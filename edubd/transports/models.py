from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.


#-----------------------driver --------------------
class Driver(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    driving_licence=models.CharField(max_length=200)
    driving_licence_validity=models.DateField(null=True)
    age=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    address=models.TextField(max_length=200, null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

#-----------------------vehicle --------------------
class Vehicle(models.Model):
    name=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    license=models.CharField(max_length=200)
    year_made=models.DateField(null=True)
    driver=models.ManyToManyField(Driver, blank=True)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 


#-----------------------stopage --------------------
class Stopage(models.Model):
    name=models.CharField(max_length=200)
    fare=models.FloatField(null=True, blank=True)
    lat=models.CharField(max_length=200, null=True, blank=True)
    long=models.CharField(max_length=200, null=True, blank=True)
    address=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

#-----------------------route --------------------
class Route(models.Model):
    name=models.CharField(max_length=200)
    start_point=models.ForeignKey(Stopage,null=True, on_delete=models.SET_NULL,related_name='start_point')
    end_point=models.ForeignKey(Stopage,null=True, on_delete=models.SET_NULL, related_name='end_point')
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#-----------------------schedule--------------------
class Schedule(models.Model):
    route=models.ForeignKey(Route,null=True, on_delete=models.SET_NULL)
    vehicle=models.ForeignKey(Vehicle,null=True, on_delete=models.SET_NULL)
    driver=models.ForeignKey(Driver,null=True, on_delete=models.SET_NULL)
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)

    
#-----------------------schedule stopage--------------------
class ScheduleStopage(models.Model):
    schedule=models.ForeignKey(Schedule,null=True,blank=True, on_delete=models.SET_NULL)
    stopage=models.ForeignKey(Stopage,null=True, on_delete=models.SET_NULL)
    reach_time=models.TimeField(null=True)
    leave_time=models.TimeField(null=True)


#-----------------------fare--------------------
class Fare(models.Model):
    start_stopage=models.ForeignKey(Stopage,null=True, on_delete=models.SET_NULL,related_name='start_stopage')
    end_stopage=models.ForeignKey(Stopage,null=True, on_delete=models.SET_NULL, related_name='end_stopage')
    fare=models.FloatField(null=True)
    date_created=models.DateTimeField(auto_now_add=True)


#-----------------------schedule member--------------------
class ScheduleMember(models.Model):
    user=models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    schedule=models.ForeignKey(Schedule,null=True,blank=True, on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True)
