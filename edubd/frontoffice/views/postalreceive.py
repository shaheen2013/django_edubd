from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User, Group
from django.urls import reverse
from ..models import Postalreceive
from ..form import PostalreceiveForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

# Create your views here.

class PostalreceiveView(View):
    def get(self,request):
        postalreceive=Postalreceive.objects.all().order_by('-id')
        contex = {'postalreceive':postalreceive}
        return render(request, 'postalreceive/index.html',contex)

class AddPostalreceiveView(View):
    def get(self,request):
        form = PostalreceiveForm()
        context = {'form':form }
        return render(request, 'postalreceive/create.html',context)
    def post(self,request):
        postalreceive=request.POST
        form = PostalreceiveForm(request.POST, request.FILES) 
        if form.is_valid():
            postalreceive=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('frontoffice:postalreceives'))
    

class EditPostalreceiveView(View):
    def get(self,request,pk):
        postalreceive=Postalreceive.objects.get(id=pk)
        form = PostalreceiveForm(instance=postalreceive)
        context={'form':form}
        return render(request, 'postalreceive/create.html',context)
    def post(self,request,pk):
        postalreceive=Postalreceive.objects.get(id=pk)
        form = PostalreceiveForm(request.POST, request.FILES, instance=postalreceive)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('frontoffice:postalreceives'))
    

class DeletePostalreceiveView(View):
    def get(self,request,pk):
        postalreceive=Postalreceive.objects.get(id=pk)
        postalreceive.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('frontoffice:postalreceives'))
