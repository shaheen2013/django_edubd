from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Fare
from ..form import FareForm
from django.contrib import messages 
# Create your views here.


class FareView(View):
    def get(self,request):
        fares=Fare.objects.all().order_by('-id')
        contex = {'fares':fares}
        return render(request, 'fare/index.html',contex)

class AddFareView(View):
    def get(self,request):
        form = FareForm()
        context = {'form':form}
        return render(request, 'fare/create.html',context)
    def post(self,request):
        fare=request.POST
        form = FareForm(request.POST) 
        if form.is_valid():
           fare=form.save()
           messages.success(request,'Data store successfull',extra_tags='success')
           return redirect(reverse('transport:fares'))
    

class EditFareView(View):
    def get(self,request,pk):
        fare=Fare.objects.get(id=pk)
        form = FareForm(instance=fare)
        context={'form':form}
        return render(request, 'fare/create.html',context)
    def post(self,request,pk):
        fare=Fare.objects.get(id=pk)
        form = FareForm(request.POST, instance=fare)
        if form.is_valid():
           form.save()
           messages.success(request,'Data update successfull',extra_tags='success')
           return redirect(reverse('transport:fares'))
    

class DeleteFareView(View):
    def get(self,request,pk):
        fare=Fare.objects.get(id=pk)
        fare.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:fares'))


