from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError

import mimetypes
import os
# Create your models here.


def validate_image(image):
    file_size = image.file.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)

def validate_file(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf','.doc', '.docx', '.jpg', '.png', '.ppt', '.pptx', '.text']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose these  %s file type' % valid_extensions)
    file_size = file.file.size
    limit_mb = 250
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)

class Visitorbook(models.Model):
    purpose=models.CharField(max_length=200, null=True )
    name=models.CharField(max_length=200, null=True )
    phone=models.CharField(max_length=200, null=True )
    meet_user_type=models.ForeignKey(Group , null=True  , on_delete=models.SET_NULL)
    meet_user=models.ForeignKey(User , null=True  , on_delete=models.SET_NULL)
    id_card=models.CharField(max_length=200, null=True )
    date=models.DateField(null=True)
    in_time=models.TimeField(null=True)
    out_time=models.TimeField(null=True, blank=True)
    note=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='visitorbook', null=True, blank=True,validators=[validate_file])
    image=models.ImageField(upload_to='visitorbook', null=True, validators=[validate_image])
    #image=FSCameraField(format='jpg')
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Phonecalllog(models.Model):
    CALL_TYPE = (
        (1, 'Incoming'),
        (2, 'Outgoing'),
    )
    name=models.CharField(max_length=200, null=True )
    phone=models.CharField(max_length=200, null=True )
    call_duration=models.CharField(max_length=200, null=True )
    date=models.DateField(null=True)
    followup=models.DateField(null=True, blank=True)
    call_type=models.IntegerField(null=True, choices=CALL_TYPE)
    description=models.TextField(null=True,blank=True)
    note=models.TextField(null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Postaldispatch(models.Model):
    receiver=models.CharField(max_length=200, null=True )
    sender=models.CharField(max_length=200, null=True )
    referance=models.CharField(max_length=200, null=True )
    dispatch_date=models.DateField(null=True)
    address=models.TextField(null=True)
    note=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='postal', null=True, blank=True,validators=[validate_file])
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receiver

class Postalreceive(models.Model):
    receiver=models.CharField(max_length=200, null=True )
    sender=models.CharField(max_length=200, null=True )
    referance=models.CharField(max_length=200, null=True )
    receive_date=models.DateField(null=True)
    address=models.TextField(null=True)
    note=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='postal', null=True, blank=True,validators=[validate_file])
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receiver

class Complain(models.Model):
    TYPE = (
        ('Fees', 'Fees'),
        ('Study', 'Study'),
        ('Teacher', 'Teacher'),
        ('Sports', 'Sports'),
        ('Transport', 'Transport'),
        ('Hostel', 'Hostel'),
        ('Front Site', 'Front Site'),
        ('Others', 'Others'),
    )
    complain_type=models.CharField(max_length=100, null=True, choices=TYPE )
    complain_by=models.ForeignKey(User , null=True  , on_delete=models.SET_NULL)
    phone=models.CharField(max_length=200, null=True )
    date=models.DateField(null=True)
    description=models.TextField(null=True,blank=True)
    action_taken=models.TextField(null=True,blank=True)
    assigned=models.ForeignKey(User , null=True, on_delete=models.SET_NULL, related_name='assigned')
    note=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='postal', null=True, blank=True,validators=[validate_file])
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.complain_type