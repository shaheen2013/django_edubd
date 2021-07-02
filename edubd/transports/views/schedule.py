from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Schedule,Stopage,ScheduleStopage,ScheduleMember
from ..form import ScheduleForm,ScheduleStopageForm, ScheduleMemberForm
from django.contrib import messages
# Create your views here.


class ScheduleView(View):
    def get(self,request):
        schedules=Schedule.objects.all().order_by('-id')
        contex = {'schedules':schedules}
        return render(request, 'schedule/index.html',contex)

class AddScheduleView(View):
    def get(self,request):
        form = ScheduleForm()
        context = {'form':form,'check':0}
        return render(request, 'schedule/create.html',context)
    def post(self,request):
        schedule=request.POST
        form = ScheduleForm(request.POST)
        if form.is_valid():
           schedule=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect(reverse('transport:schedules'))
    

class EditScheduleView(View):
    def get(self,request,pk):
        schedule=Schedule.objects.get(id=pk)
        form = ScheduleForm(instance=schedule)
        context={'form':form,'check':1}
        return render(request, 'schedule/create.html',context)
    def post(self,request,pk):
        schedule=Schedule.objects.get(id=pk)
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect(reverse('transport:schedules'))
    

class DeleteScheduleView(View):
    def get(self,request,pk):
        schedule=Schedule.objects.get(id=pk)
        schedule.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:schedules'))

class ScheduleStopageView(View):
    def get(self,request,pk):
        stopages=ScheduleStopage.objects.filter(schedule=pk).all()
        contex = {'stopages':stopages,'schedule':pk}
        return render(request, 'schedule/stopage.html',contex)

class AddScheduleStopageView(View):
    def get(self,request,pk):
        form=ScheduleStopageForm()
        stopage=Stopage.objects.all()
        context={'form':form,'schedule':pk, 'stopage':stopage}
        return render(request, 'schedule/add_stopage.html',context)
    def post(self,request,pk):
        schedule=Schedule.objects.get(id=pk)
        reach_time=request.POST.get('reach_time')
        leave_time=request.POST.get('leave_time')
        form = ScheduleStopageForm(request.POST)
        if form.is_valid():
           for row in request.POST.getlist('stopage'):
               stopage=Stopage.objects.get(id=row)
               ScheduleStopage.objects.create(schedule=schedule, stopage=stopage, reach_time=reach_time, leave_time=leave_time)
               #schedule=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect(reverse('transport:schedule_stopages', args=[pk]))
    


class DeleteScheduleStopageView(View):
    def get(self,request,pk):
        schedule=ScheduleStopage.objects.get(id=pk)
        schedule.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:schedule_stopages', args=[schedule.schedule.id]))


class ScheduleMemberView(View):
    def get(self,request,pk):
        members=ScheduleMember.objects.filter(schedule=pk).all()
        contex = {'members':members,'schedule':pk}
        return render(request, 'schedule/member.html',contex)

class AddScheduleMemberView(View):
    def get(self,request,pk):
        form=ScheduleMemberForm()
        context={'form':form,'schedule':pk}
        return render(request, 'schedule/add_member.html',context)
    def post(self,request,pk):
        schedule=Schedule.objects.get(id=pk)
        #if form.is_valid():
        if request.POST.getlist('user'):
            for row in request.POST.getlist('user'):
                print(row)
                if row:
                    print(row)
                    user=User.objects.get(id=row)
                    ScheduleMember.objects.create(schedule=schedule, user=user)
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('transport:schedule_members', args=[pk]))
        messages.success(request,'Please select a member',extra_tags='error')
        return redirect(reverse('transport:add_schedule_membre', args=[pk]))
    


class DeleteScheduleMemberView(View):
    def get(self,request,pk):
        schedule=ScheduleMember.objects.get(id=pk)
        schedule.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:schedule_members', args=[schedule.schedule.id]))