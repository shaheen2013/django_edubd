from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Notice
from ..form import NoticeForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

class NoticeView(View):
    def get(self,request):
        notices=Notice.objects.all().order_by('-id')
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        contex = {'notices':notices,'date':date}
        return render(request, 'notice/index.html',contex)

class AddNoticeView(View):
    def get(self,request):
        form = NoticeForm()
        context = {'form':form}
        return render(request, 'notice/create.html',context)
    def post(self,request):
        notice=request.POST
        form = NoticeForm(request.POST, request.FILES) 
        if form.is_valid():
            notice=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('announcement:notices'))
    

class DetailNoticeView(View):
    def get(self,request,pk):
        notice=Notice.objects.get(id=pk)
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        context={'notice':notice,'date':date}
        return render(request, 'notice/detail.html',context)

class EditNoticeView(View):
    def get(self,request,pk):
        notice=Notice.objects.get(id=pk)
        form = NoticeForm(instance=notice)
        context={'form':form}
        return render(request, 'notice/create.html',context)
    def post(self,request,pk):
        notice=Notice.objects.get(id=pk)
        form = NoticeForm(request.POST, request.FILES, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('announcement:notices'))
    

class DeleteNoticeView(View):
    def get(self,request,pk):
        notice=Notice.objects.get(id=pk)
        notice.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('announcement:notices'))

class ApprovNoticeView(View):
    def get(self,request,pk):
        Notice.objects.filter(pk=pk).update(approve_status=1)
        messages.success(request,'Data approve successfull',extra_tags='success')
        return redirect(reverse('notice:list'))

class DeclineNoticeView(View):
    def get(self,request,pk):
        Notice.objects.filter(pk=pk).update(approve_status=2)
        messages.success(request,'Data decline successfull',extra_tags='success')
        return redirect(reverse('notice:list'))

