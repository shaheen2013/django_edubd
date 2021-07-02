from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import News
from ..form import NewsForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

class NewsView(View):
    def get(self,request):
        news=News.objects.all().order_by('-id')
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        contex = {'news':news,'date':date}
        return render(request, 'news/index.html',contex)

class AddNewsView(View):
    def get(self,request):
        form = NewsForm()
        context = {'form':form}
        return render(request, 'news/create.html',context)
    def post(self,request):
        news=request.POST
        form = NewsForm(request.POST, request.FILES) 
        if form.is_valid():
            news=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('announcement:news'))
    

class DetailNewsView(View):
    def get(self,request,pk):
        news=News.objects.get(id=pk)
        date=formats.date_format(datetime.datetime.now().date(),'Y-m-d')
        context={'news':news,'date':date}
        return render(request, 'news/detail.html',context)

class EditNewsView(View):
    def get(self,request,pk):
        news=News.objects.get(id=pk)
        form = NewsForm(instance=news)
        context={'form':form}
        return render(request, 'news/create.html',context)
    def post(self,request,pk):
        news=News.objects.get(id=pk)
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('announcement:news'))
    

class DeleteNewsView(View):
    def get(self,request,pk):
        news=News.objects.get(id=pk)
        news.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('announcement:news'))

class ApprovNewsView(View):
    def get(self,request,pk):
        News.objects.filter(pk=pk).update(approve_status=1)
        messages.success(request,'Data approve successfull',extra_tags='success')
        return redirect(reverse('news:list'))

class DeclineNewsView(View):
    def get(self,request,pk):
        News.objects.filter(pk=pk).update(approve_status=2)
        messages.success(request,'Data decline successfull',extra_tags='success')
        return redirect(reverse('news:list'))

