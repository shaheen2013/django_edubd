from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from ..models import HostelType
from ..form import HostelTypeForm
#from .form import *
from django.contrib import messages
# Create your views here.


def hostel_type(request):
    hostel_types=HostelType.objects.all().order_by('-id')
    form = HostelTypeForm()
    if request.method=='POST':
        hostel_type=request.POST
        form = HostelTypeForm(request.POST) 
        if form.is_valid():
           hostel_type=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/hostel_type_list')
    contex = {'hostel_types':hostel_types, 'form':form}
    return render(request, 'hosteltype/index.html',contex)


def hostel_type_edit(request, pk):
    hostel_types=HostelType.objects.all().order_by('-id')
    hostel_type=HostelType.objects.get(id=pk)
    form = HostelTypeForm(instance=hostel_type)
    if request.method=='POST':
        form = HostelTypeForm(request.POST, instance=hostel_type)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/hostel_type_list')
    context={'form':form, 'hostel_types':hostel_types}
    return render(request, 'hosteltype/index.html',context)

def hostel_type_delete(request,pk):
    hostel_type=HostelType.objects.get(id=pk)
    hostel_type.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/hostel_type_list')