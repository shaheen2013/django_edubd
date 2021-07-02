from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from ..models import Route
from ..form import RouteForm
from django.contrib import messages 
# Create your views here.

class RouteView(View):
    def get(self,request):
        routes=Route.objects.all().order_by('-id')
        contex = {'routes':routes}
        return render(request, 'route/index.html',contex)

class AddRouteView(View):
    def get(self,request):
        form = RouteForm()
        context = {'form':form}
        return render(request, 'route/create.html',context)
    def post(self,request):
        if request.method=='POST':
            route=request.POST
            form = RouteForm(request.POST) 
            if form.is_valid():
                route=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('transport:routes'))
    

class EditRouteView(View):
    def get(self,request,pk):
        route=Route.objects.get(id=pk)
        form = RouteForm(instance=route)
        context={'form':form}
        return render(request, 'route/create.html',context)
    def post(self,request,pk):
        route=Route.objects.get(id=pk)
        if request.method=='POST':
            form = RouteForm(request.POST, instance=route)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('transport:routes'))
    

class DeleteRouteView(View):
    def get(self,request,pk):
        route=Route.objects.get(id=pk)
        route.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('transport:routes'))