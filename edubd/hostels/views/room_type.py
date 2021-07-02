from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from ..models import RoomType
from ..form import RoomTypeForm
#from .form import *
from django.contrib import messages
# Create your views here.


def room_type(request):
    room_types=RoomType.objects.all().order_by('-id')
    form = RoomTypeForm()
    if request.method=='POST':
        room_type=request.POST
        form = RoomTypeForm(request.POST) 
        if form.is_valid():
           room_type=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/room_type_list')
    contex = {'room_types':room_types, 'form':form}
    return render(request, 'roomtype/index.html',contex)


def room_type_edit(request, pk):
    room_types=RoomType.objects.all().order_by('-id')
    room_type=RoomType.objects.get(id=pk)
    form = RoomTypeForm(instance=room_type)
    if request.method=='POST':
        form = RoomTypeForm(request.POST, instance=room_type)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/room_type_list')
    context={'form':form, 'room_types':room_types}
    return render(request, 'roomtype/index.html',context)

def room_type_delete(request,pk):
    room_type=RoomType.objects.get(id=pk)
    room_type.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/room_type_list')