from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User, Group
from django.urls import reverse
from ..models import Phonecalllog
from ..form import PhonecalllogForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

# Create your views here.

class PhonecalllogView(View):
    def get(self,request):
        phonecalllog=Phonecalllog.objects.all().order_by('-id')
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        contex = {'phonecalllog':phonecalllog,'date':date}
        return render(request, 'phonecalllog/index.html',contex)

class AddPhonecalllogView(View):
    def get(self,request):
        form = PhonecalllogForm()
        context = {'form':form }
        return render(request, 'phonecalllog/create.html',context)
    def post(self,request):
        phonecalllog=request.POST
        form = PhonecalllogForm(request.POST, request.FILES) 
        if form.is_valid():
            phonecalllog=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('frontoffice:phonecalllogs'))
    

class DetailPhonecalllogView(View):
    def get(self,request,pk):
        phonecalllog=Phonecalllog.objects.get(id=pk)
        context={'phonecalllog':phonecalllog}
        return render(request, 'phonecalllog/detail.html',context)

class EditPhonecalllogView(View):
    def get(self,request,pk):
        phonecalllog=Phonecalllog.objects.get(id=pk)
        form = PhonecalllogForm(instance=phonecalllog)
        context={'form':form}
        return render(request, 'phonecalllog/create.html',context)
    def post(self,request,pk):
        phonecalllog=Phonecalllog.objects.get(id=pk)
        form = PhonecalllogForm(request.POST, request.FILES, instance=phonecalllog)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('frontoffice:phonecalllogs'))
    

class DeletePhonecalllogView(View):
    def get(self,request,pk):
        phonecalllog=Phonecalllog.objects.get(id=pk)
        phonecalllog.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('frontoffice:phonecalllogs'))

