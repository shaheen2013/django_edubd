from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Type
from ..form import TypeForm
from django.contrib import messages
# Create your views here.

class TypeView(View):
    def get(self,request):
        types=Type.objects.all().order_by('-id')
        form = TypeForm()
        contex = {'types':types, 'form':form}
        return render(request, 'type/index.html',contex)

    def post(self,request):
        types=Type.objects.all().order_by('-id')
        type=request.POST
        form = TypeForm(request.POST) 
        if form.is_valid():
            type=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('leave:types'))
    
class EditTypeView(View):
    def get(self,request,pk):
        types=Type.objects.all().order_by('-id')
        type=Type.objects.get(id=pk)
        form = TypeForm(instance=type)
        context={'form':form, 'types':types}
        return render(request, 'type/index.html',context)
    def post(self,request,pk):
        type=Type.objects.get(id=pk)
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('leave:types'))
    

class DeleteTypeView(View):
    def get(self,request,pk):
        type=Type.objects.get(id=pk)
        type.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('leave:types'))

