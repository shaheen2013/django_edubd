from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User, Group
from django.urls import reverse
from ..models import Complain
from ..form import ComplainForm
from django.contrib import messages
import datetime
from django.utils import formats


# Create your views here.

# Create your views here.

class ComplainView(View):
    def get(self,request):
        complain=Complain.objects.all().order_by('-id')
        contex = {'complain':complain}
        return render(request, 'complain/index.html',contex)

class AddComplainView(View):
    def get(self,request):
        form = ComplainForm()
        context = {'form':form, 'check':0}
        return render(request, 'complain/create.html',context)
    def post(self,request):
        complain=request.POST
        form = ComplainForm(request.POST, request.FILES) 
        if form.is_valid():
            complain=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('frontoffice:complains'))
    

class DetailComplainView(View):
    def get(self,request,pk):
        complain=Complain.objects.get(id=pk)
        context={'complain':complain}
        return render(request, 'complain/detail.html',context)

class EditComplainView(View):
    def get(self,request,pk):
        complain=Complain.objects.get(id=pk)
        form = ComplainForm(instance=complain)
        context={'form':form, 'check':1}
        return render(request, 'complain/create.html',context)
    def post(self,request,pk):
        complain=Complain.objects.get(id=pk)
        form = ComplainForm(request.POST, request.FILES, instance=complain)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('frontoffice:complains'))
    

class DeleteComplainView(View):
    def get(self,request,pk):
        complain=Complain.objects.get(id=pk)
        complain.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('frontoffice:complains'))



class GetUserView(View):
    def get(self,request):
        id=request.GET.get('id')
        users=User.objects.filter(groups=id).all()
        print(users)
        context={'users':users}
        return render(request, 'complain/get_user.html',context)