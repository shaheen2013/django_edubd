from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Vehicle,Driver
from ..form import VehicleForm
from django.contrib import messages
# Create your views here.


class VehiclesView(View):
    def get(self,request):
        vehicles=Vehicle.objects.all().order_by('-id')
        contex = {'vehicles':vehicles}
        return render(request, 'vehicle/index.html',contex)

class AddVehicleView(View):
    def get(self,request):
        form = VehicleForm()
        context = {'form':form}
        return render(request, 'vehicle/create.html',context)
    def post(self,request):
        if request.method=='POST':
            vehicle=request.POST
            form = VehicleForm(request.POST) 
            if form.is_valid():
                vehicle=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('transport:vehicles'))
        

class EditVehicleView(View):
    def get(self,request,pk):
        vehicle=Vehicle.objects.get(id=pk)
        form = VehicleForm(instance=vehicle)
        context={'form':form}
        return render(request, 'vehicle/create.html',context)
    def post(self,request,pk):
        vehicle=Vehicle.objects.get(id=pk)
        if request.method=='POST':
            form = VehicleForm(request.POST, instance=vehicle)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('transport:vehicles'))
    

class DeleteVehicleView(View):
    def get(self,request,pk):
        vehicle=Vehicle.objects.get(id=pk)
        vehicle.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:vehicles'))


class VehicleDriversView(View):
    def get(self,request,pk):
        drivers=Driver.objects.filter(vehicle=pk).all()
        contex = {'drivers':drivers,'vehicle':pk}
        return render(request, 'vehicle/driver.html',contex)

class AddVehicleDriverView(View):
    def get(self,request,pk):
        vehicle=Vehicle.objects.get(id=pk)
        driver = Driver.objects.all()
        context={'driver':driver}
        return render(request, 'vehicle/add_driver.html',context)
    def post(self,request,pk):
        vehicle=Vehicle.objects.get(id=pk)
        if request.method=='POST':
            if request.POST.getlist('driver_id'):
                for row in request.POST.getlist('driver_id'):
                    driver1 = Driver.objects.filter(id=row).get()
                    vehicle.driver.add(driver1)
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('transport:vehicle_drivers', args=[pk]))
            else:
                messages.success(request,'please select a driver',extra_tags='error')
                return redirect(reverse('transport:add_vehicle_driver', args=[pk]))
    

class DeleteVehicleDriverView(View):
    def get(self,request,vehicle,driver):
        hostel=Vehicle.objects.get(id=vehicle)
        driver=Driver.objects.get(id=driver)
        hostel.driver.remove(driver)
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:vehicle_drivers', args=[vehicle]))


class GetDriverView(View):
    def get(self,request):
        vehicle=request.GET.get('vehicle')
        drivers=Driver.objects.filter(vehicle=vehicle).all()
        context={'drivers':drivers}
        return render(request, 'schedule/get_driver.html',context)