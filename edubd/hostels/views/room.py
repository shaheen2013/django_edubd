from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from ..models import Room, RoomType
from ..form import RoomForm
#from .form import *
from django.contrib import messages
# Create your views here.


def room(request):
    rooms=Room.objects.all().order_by('-id')
    form = RoomForm()
    if request.method=='POST':
        room=request.POST
        form = RoomForm(request.POST) 
        if form.is_valid():
           room=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/room_list')
    contex = {'rooms':rooms, 'form':form}
    return render(request, 'room/index.html',contex)

def room_create(request):
    form = RoomForm()
    if request.method=='POST':
        room=request.POST
        form = RoomForm(request.POST) 
        if form.is_valid():
           room=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/room_list')
    context = {'form':form}
    return render(request, 'room/create.html',context)

def room_edit(request, pk):
    room=Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method=='POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/room_list')
    context={'form':form}
    return render(request, 'room/create.html',context)

def room_delete(request,pk):
    room=Room.objects.get(id=pk)
    room.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/room_list')