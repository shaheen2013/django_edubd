from django.db import models
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
import mimetypes
import os
# Create your models here.

def validate_file(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf','.doc', '.docx', '.jpg', '.png', '.ppt', '.pptx', '.text']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose these  %s file type' % valid_extensions)
    file_size = file.file.size
    limit_mb = 250
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)

class Notice(models.Model):
    STATUS = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    notice_for=models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=200, null=True )
    active_date=models.DateField(null=True, blank=True)
    description=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='notice', null=True, blank=True,validators=[validate_file])
    status=models.IntegerField(null=True, choices=STATUS)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

class News(models.Model):
    STATUS = (
        (0, 'Inactive'),
        (1, 'Active'),
    )
    notice_for=models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=200, null=True )
    active_date=models.DateField(null=True, blank=True)
    description=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='notice', null=True, blank=True,validators=[validate_file])
    status=models.IntegerField(null=True, choices=STATUS)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 


class Holiday(models.Model):
    title=models.CharField(max_length=200, null=True )
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    description=models.TextField(null=True,blank=True)
    attachment=models.FileField(upload_to='holiday', null=True, blank=True,validators=[validate_file])
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 