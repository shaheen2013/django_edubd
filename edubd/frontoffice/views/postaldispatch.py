from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User, Group
from django.urls import reverse
from ..models import Postaldispatch
from ..form import PostaldispatchForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

# Create your views here.

class PostaldispatchView(View):
    def get(self,request):
        postaldispatch=Postaldispatch.objects.all().order_by('-id')
        contex = {'postaldispatch':postaldispatch}
        return render(request, 'postaldispatch/index.html',contex)

class AddPostaldispatchView(View):
    def get(self,request):
        form = PostaldispatchForm()
        context = {'form':form }
        return render(request, 'postaldispatch/create.html',context)
    def post(self,request):
        postaldispatch=request.POST
        form = PostaldispatchForm(request.POST, request.FILES) 
        if form.is_valid():
            postaldispatch=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('frontoffice:postaldispatchs'))
    



class EditPostaldispatchView(View):
    def get(self,request,pk):
        postaldispatch=Postaldispatch.objects.get(id=pk)
        form = PostaldispatchForm(instance=postaldispatch)
        context={'form':form}
        return render(request, 'postaldispatch/create.html',context)
    def post(self,request,pk):
        postaldispatch=Postaldispatch.objects.get(id=pk)
        form = PostaldispatchForm(request.POST, request.FILES, instance=postaldispatch)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('frontoffice:postaldispatchs'))
    

class DeletePostaldispatchView(View):
    def get(self,request,pk):
        postaldispatch=Postaldispatch.objects.get(id=pk)
        postaldispatch.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('frontoffice:postaldispatchs'))

