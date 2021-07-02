from django import template
from django.contrib.auth.models import Group 
from ..models import BookIssue, Book
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False

@register.simple_tag
def abc():
    #print(request.user)
    return "kk"

@register.simple_tag
def available_qty(id):
    total=Book.objects.filter(id=id).get()
    available_qty=BookIssue.objects.filter(book=id, status=0).count()
    return total.qty-available_qty

