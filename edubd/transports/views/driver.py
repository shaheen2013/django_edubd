from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Driver
from ..form import DriverForm
from django.contrib import messages
# Create your views here.

class DriversView(View):
    def get(self,request):
        drivers=Driver.objects.all().order_by('-id')
        contex = {'drivers':drivers}
        return render(request, 'driver/index.html',contex)

class AddDriverView(View):
    def get(self,request):
        form = DriverForm()
        context = {'form':form}
        return render(request, 'driver/create.html',context)
    def post(self,request):
        if request.method=='POST':
            driver=request.POST
            form = DriverForm(request.POST) 
            if form.is_valid():
                driver=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('transport:drivers'))
    

class EditDriverView(View):
    def get(self,request,pk):
        driver=Driver.objects.get(id=pk)
        form = DriverForm(instance=driver)
        context={'form':form}
        return render(request, 'driver/create.html',context)
    def post(self,request,pk):
        driver=Driver.objects.get(id=pk)
        if request.method=='POST':
            form = DriverForm(request.POST, instance=driver)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('transport:drivers'))
    

class DeleteDriverView(View):
    def get(self,request,pk):
        driver=Driver.objects.get(id=pk)
        driver.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:drivers'))

