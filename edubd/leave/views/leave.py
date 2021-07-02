from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Leave
from ..form import LeaveForm
from django.contrib import messages
# Create your views here.

class LeaveView(View):
    def get(self,request):
        leaves=Leave.objects.all().order_by('-id')
        contex = {'leaves':leaves}
        return render(request, 'leave/index.html',contex)

class AddLeaveView(View):
    def get(self,request):
        form = LeaveForm()
        context = {'form':form}
        return render(request, 'leave/create.html',context)
    def post(self,request):
        request.POST=request.POST.copy()
        request.POST['applied_by']=request.user.id
        request.POST['role']=1
        form = LeaveForm(request.POST, request.FILES) 
        if form.is_valid():
            leave=form.save()
            messages.success(request,'Data store successfull',extra_tags='success')
            return redirect(reverse('leave:list'))
    

class EditLeaveView(View):
    def get(self,request,pk):
        leave=Leave.objects.get(id=pk)
        form = LeaveForm(instance=leave)
        context={'form':form}
        return render(request, 'leave/create.html',context)
    def post(self,request,pk):
        leave=Leave.objects.get(id=pk)
        request.POST=request.POST.copy()
        request.POST['applied_by']=request.user.id
        request.POST['role']=1
        form = LeaveForm(request.POST, request.FILES, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request,'Data update successfull',extra_tags='success')
            return redirect(reverse('leave:list'))
    

class DeleteLeaveView(View):
    def get(self,request,pk):
        leave=Leave.objects.get(id=pk)
        leave.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('leave:list'))

class ApprovLeaveView(View):
    def get(self,request,pk):
        Leave.objects.filter(pk=pk).update(approve_status=1)
        messages.success(request,'Data approve successfull',extra_tags='success')
        return redirect(reverse('leave:list'))

class DeclineLeaveView(View):
    def get(self,request,pk):
        Leave.objects.filter(pk=pk).update(approve_status=2)
        messages.success(request,'Data decline successfull',extra_tags='success')
        return redirect(reverse('leave:list'))

