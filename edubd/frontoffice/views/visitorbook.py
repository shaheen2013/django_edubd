from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User, Group
from django.urls import reverse
from ..models import Visitorbook
from ..form import VisitorbookForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

# Create your views here.

class VisitorbookView(View):
    def get(self,request):
        visitorbook=Visitorbook.objects.all().order_by('-id')
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        contex = {'visitorbook':visitorbook,'date':date}
        return render(request, 'visitorbook/index.html',contex)

class AddVisitorbookView(View):
    def get(self,request):
        form = VisitorbookForm()
        context = {'form':form, 'check':0}
        return render(request, 'visitorbook/create.html',context)
    def post(self,request):
        visitorbook=request.POST
        form = VisitorbookForm(request.POST, request.FILES) 
        if form.is_valid():
            visitorbook=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('frontoffice:visitorbooks'))
    

class DetailVisitorbookView(View):
    def get(self,request,pk):
        visitorbook=Visitorbook.objects.get(id=pk)
        context={'visitorbook':visitorbook}
        return render(request, 'visitorbook/detail.html',context)

class EditVisitorbookView(View):
    def get(self,request,pk):
        visitorbook=Visitorbook.objects.get(id=pk)
        form = VisitorbookForm(instance=visitorbook)
        context={'form':form, 'check':1}
        return render(request, 'visitorbook/create.html',context)
    def post(self,request,pk):
        visitorbook=Visitorbook.objects.get(id=pk)
        form = VisitorbookForm(request.POST, request.FILES, instance=visitorbook)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('frontoffice:visitorbooks'))
    

class DeleteVisitorbookView(View):
    def get(self,request,pk):
        visitorbook=Visitorbook.objects.get(id=pk)
        visitorbook.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('frontoffice:visitorbooks'))



class GetUserView(View):
    def get(self,request):
        id=request.GET.get('id')
        users=User.objects.filter(groups=id).all()
        print(users)
        context={'users':users}
        return render(request, 'visitorbook/get_user.html',context)