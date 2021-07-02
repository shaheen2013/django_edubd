from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Holiday
from ..form import HolidayForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

class HolidayView(View):
    def get(self,request):
        holiday=Holiday.objects.all().order_by('-id')
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        contex = {'holiday':holiday,'date':date}
        return render(request, 'holiday/index.html',contex)

class AddHolidayView(View):
    def get(self,request):
        form = HolidayForm()
        context = {'form':form}
        return render(request, 'holiday/create.html',context)
    def post(self,request):
        holiday=request.POST
        form = HolidayForm(request.POST, request.FILES) 
        if form.is_valid():
            holiday=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('announcement:holidays'))
    

class DetailHolidayView(View):
    def get(self,request,pk):
        holiday=Holiday.objects.get(id=pk)
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        context={'holiday':holiday,'date':date}
        return render(request, 'holiday/detail.html',context)

class EditHolidayView(View):
    def get(self,request,pk):
        holiday=Holiday.objects.get(id=pk)
        form = HolidayForm(instance=holiday)
        context={'form':form}
        return render(request, 'holiday/create.html',context)
    def post(self,request,pk):
        holiday=Holiday.objects.get(id=pk)
        form = HolidayForm(request.POST, request.FILES, instance=holiday)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('announcement:holidays'))
    

class DeleteHolidayView(View):
    def get(self,request,pk):
        holiday=Holiday.objects.get(id=pk)
        holiday.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('announcement:holidays'))

class ApprovHolidayView(View):
    def get(self,request,pk):
        Holiday.objects.filter(pk=pk).update(approve_status=1)
        messages.success(request,'Data approve successfull',extra_tags='success')
        return redirect(reverse('holiday:list'))

class DeclineHolidayView(View):
    def get(self,request,pk):
        Holiday.objects.filter(pk=pk).update(approve_status=2)
        messages.success(request,'Data decline successfull',extra_tags='success')
        return redirect(reverse('holiday:list'))

