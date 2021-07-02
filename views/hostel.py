from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Hostel, HostelType, Room, HostelRoomStudent, HostelStaff, Designation
from ..form import HostelForm 
from django.contrib import messages
# Create your views here.


def hostel(request):
    hostels=Hostel.objects.all().order_by('-id')
    form = HostelForm()
    if request.method=='POST':
        hostel=request.POST
        form = HostelForm(request.POST) 
        if form.is_valid():
           hostel=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/hostel_list')
    contex = {'hostels':hostels, 'form':form}
    return render(request, 'hostel/index.html',contex)
def hostel_view(request, pk):
    hostel=Hostel.objects.get(id=pk)
    context={'hostel':hostel}
    return render(request, 'hostel/view.html',context)

def hostel_create(request):
    form = HostelForm()
    if request.method=='POST':
        hostel=request.POST
        form = HostelForm(request.POST) 
        if form.is_valid():
           hostel=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect('/hostel_list')
    context = {'form':form}
    return render(request, 'hostel/create.html',context)

def hostel_edit(request, pk):
    hostel=Hostel.objects.get(id=pk)
    form = HostelForm(instance=hostel)
    if request.method=='POST':
        form = HostelForm(request.POST, instance=hostel)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect('/hostel_list')
    context={'form':form}
    return render(request, 'hostel/create.html',context)



def hostel_delete(request,pk):
    hostel=Hostel.objects.get(id=pk)
    hostel.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect('/hostel_list')


def hostel_room(request,pk):
    rooms=Room.objects.filter(hostel=pk).all()
    context={'rooms':rooms,'hostel_id':pk}
    return render(request, 'hostel/hostel_room.html',context)

def hostel_add_room(request, pk):
    hostel=Hostel.objects.get(id=pk)
    room = Room.objects.all()
    if request.method=='POST':
        if request.POST.getlist('room_id'):
            for row in request.POST.getlist('room_id'):
                room1 = Room.objects.filter(id=row).get()
                hostel.room.add(room1)
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('hostel.room', args=[pk]))
        else:
            messages.success(request,'please select a room',extra_tags='error')
            return redirect(reverse('hostel.add_room', args=[pk]))
    context={'room':room}
    return render(request, 'hostel/add_room.html',context)


def hostel_room_delete(request,pk,room):
    hostel=Hostel.objects.get(id=pk)
    room1=Room.objects.get(id=room)
    hostel.room.remove(room1)
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect(reverse('hostel.room', args=[pk]))



def student(request,hostel,room):
    student=HostelRoomStudent.objects.filter(hostel=hostel, room=room).all()
    context={'student':student}
    return render(request, 'hostel/student.html',context)

def add_student(request, pk):
    student=User.objects.all()
    rooms=Room.objects.filter(hostel=pk).all()
    if request.method=='POST':
        if not (request.POST.get('room_id') or request.POST.get('hostel_id') or request.POST.get('user_id')):
            messages.success(request,'please select al the field',extra_tags='error')
            return redirect('hostel_list')
        room=Room.objects.filter(id=request.POST.get('room_id')).get()
        hostel=Hostel.objects.filter(id=request.POST.get('hostel_id')).get()
        room_member=HostelRoomStudent.objects.filter(hostel=hostel, room=room).count()
        
        if room.number_of_bed <= room_member:
            messages.success(request,'No space in this room',extra_tags='error')
            return redirect(reverse('hostel.add_student', args=[pk]))
        user=User.objects.filter(id=request.POST.get('user_id')).get()
        check_user=HostelRoomStudent.objects.filter(user=user)
        if check_user:
           messages.success(request,'User Already assingned',extra_tags='error')
           return redirect(reverse('hostel.add_student', args=[pk]))
        data=HostelRoomStudent(user=user,room=room,hostel=hostel)
        data.save()
        messages.success(request,'Data store successfull',extra_tags='success')
        return redirect(reverse('hostel.room', args=[pk]))
    context={'rooms':rooms,'student':student,'hostel_id':pk}
    return render(request, 'hostel/add_student.html',context)


def student_delete(request,pk):
    student=HostelRoomStudent.objects.get(id=pk)
    student.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect(reverse('hostel.student', args=[student.hostel.id,student.room.id]))



def staff(request,hostel):
    staff=HostelStaff.objects.filter(hostel=hostel).all()
    context={'staff':staff,'hostel':hostel}
    return render(request, 'hostel/staff.html',context)

def add_staff(request, pk):
    staff=User.objects.all()
    designation=Designation.objects.all()
    if request.method=='POST':
        if not (request.POST.get('designation') or request.POST.get('hostel_id') or request.POST.get('user_id')):
            messages.success(request,'please select al the field',extra_tags='error')
            return redirect(reverse('hostel.add_staff', args=[pk]))
        designation=Designation.objects.filter(id=request.POST.get('designation')).get()
        hostel=Hostel.objects.filter(id=request.POST.get('hostel_id')).get()
        user=User.objects.filter(id=request.POST.get('user_id')).get()
        data=HostelStaff(user=user,designation=designation,hostel=hostel)
        data.save()
        messages.success(request,'Data store successfull',extra_tags='success')
        return redirect(reverse('hostel.staff', args=[pk]))
    context={'designation':designation,'staff':staff,'hostel_id':pk}
    return render(request, 'hostel/add_staff.html',context)


def staff_delete(request,pk):
    staff=HostelStaff.objects.get(id=pk)
    staff.delete()
    messages.success(request,'Data delete successfull',extra_tags='success')
    return redirect(reverse('hostel.staff', args=[staff.hostel.id]))