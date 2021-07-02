from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Stopage
from ..form import StopageForm
from django.contrib import messages 
# Create your views here.


class StopageView(View):
    def get(self,request):
        stopages=Stopage.objects.all().order_by('-id')
        contex = {'stopages':stopages}
        return render(request, 'stopage/index.html',contex)

class AddStopageView(View):
    def get(self,request):
        form = StopageForm()
        context = {'form':form}
        return render(request, 'stopage/create.html',context)
    def post(self,request):
        if request.method=='POST':
            stopage=request.POST
            form = StopageForm(request.POST) 
            if form.is_valid():
                stopage=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('transport:stopages'))
    
class EditStopageView(View):
    def get(self,request,pk):
        stopage=Stopage.objects.get(id=pk)
        form = StopageForm(instance=stopage)
        context={'form':form}
        return render(request, 'stopage/create.html',context)
    def post(self,request,pk):
        stopage=Stopage.objects.get(id=pk)
        if request.method=='POST':
            form = StopageForm(request.POST, instance=stopage)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('transport:stopages'))
        

class DeleteStopageView(View):
    def get(self,request,pk):
        stopage=Stopage.objects.get(id=pk)
        stopage.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:stopages'))