from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import mimetypes
import os

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

#---------------------publisher------------------------------
class Publisher(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 


#---------------------subject------------------------------
class Subject(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#---------------------book language------------------------------
class BookLanguage(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=200, null=True, blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#---------------------rack number------------------------------
class Rack(models.Model):
    name=models.CharField(max_length=200)
    number=models.IntegerField(null=True, unique=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


#---------------------book------------------------------
def validate_image(image):
    file_size = image.file.size
    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)

class Book(models.Model):
    title=models.CharField(max_length=200, null=True)
    book_number=models.CharField(max_length=200,  null=True)
    isbn_number=models.CharField(max_length=200,  null=True)
    price=models.FloatField(null=True)
    qty=models.IntegerField(null=True)
    publisher=models.ForeignKey(Publisher,null=True, on_delete=models.SET_NULL)
    author=models.ForeignKey(Author,null=True, on_delete=models.SET_NULL)
    subject=models.ForeignKey(Subject,null=True, on_delete=models.SET_NULL)
    book_language=models.ForeignKey(BookLanguage,null=True, on_delete=models.SET_NULL)
    rack=models.ForeignKey(Rack,null=True, on_delete=models.SET_NULL)
    description=models.TextField(null=True, blank=True)
    image=models.ImageField(null=True, validators=[validate_image])
    status=models.IntegerField(default=0, null=True, blank=True)
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


#---------------------e-book------------------------------
def validate_file(file):
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf','.doc', '.docx', '.jpg', '.png', '.ppt', '.pptx', '.text']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Please choose these  %s file type' % valid_extensions)
    file_size = file.file.size
    limit_mb = 250
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)
   
    

class EBook(models.Model):
    title=models.CharField(max_length=200, null=True)
    book_number=models.CharField(max_length=200,  null=True)
    isbn_number=models.CharField(max_length=200,  null=True)
    price=models.FloatField(null=True)
    publisher=models.ForeignKey(Publisher,null=True, on_delete=models.SET_NULL)
    author=models.ForeignKey(Author,null=True, on_delete=models.SET_NULL)
    subject=models.ForeignKey(Subject,null=True, on_delete=models.SET_NULL)
    book_language=models.ForeignKey(BookLanguage,null=True, on_delete=models.SET_NULL)
    description=models.TextField(null=True, blank=True)
    image=models.ImageField(null=True, validators=[validate_image])
    file=models.FileField(upload_to='ebook', null=True, validators=[validate_file])
    status=models.IntegerField(default=0, null=True, blank=True)
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



#---------------------book issue------------------------------

class BookIssue(models.Model):
    member=models.ForeignKey(User, related_name='member', null=True, on_delete=models.SET_NULL)
    issued_by=models.ForeignKey(User, related_name='issued_by', null=True, on_delete=models.SET_NULL, blank=True)
    book=models.ForeignKey(Book,null=True, on_delete=models.SET_NULL)
    note=models.TextField(null=True, blank=True)
    status=models.IntegerField(default=0, null=True, blank=True)
    issue_date=models.DateTimeField(null=True)
    return_date=models.DateTimeField(null=True)

    def __int__(self):
        return self.member