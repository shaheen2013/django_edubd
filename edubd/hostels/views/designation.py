from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from ..models import Designation
from ..form import DesignationForm
#from .form import *
from django.contrib import messages
# Create your views here.


def index(request):
    designations=Designation.objects.all().order_by('-id')
    form = DesignationForm()
    if request.method=='POST':
        designation=request.POST
        form = DesignationForm(request.POST) 
        if form.is_valid():
           designation=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/designation_list')
    contex = {'designations':designations, 'form':form}
    return render(request, 'designation/index.html',contex)


def edit(request, pk):
    designations=Designation.objects.all().order_by('-id')
    designation=Designation.objects.get(id=pk)
    form = DesignationForm(instance=designation)
    if request.method=='POST':
        form = DesignationForm(request.POST, instance=designation)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/designation_list')
    context={'form':form, 'designations':designations}
    return render(request, 'designation/index.html',context)

def delete(request,pk):
    designation=Designation.objects.get(id=pk)
    designation.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/designation_list')