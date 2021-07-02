from django import template
from django.contrib.auth.models import Group 
from ..models import Room, HostelRoomStudent
register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False

@register.simple_tag
def abc():
    #print(request.user)
    return "kkj"

@register.simple_tag
def available_seat(id, hostel):
    total=Room.objects.filter(id=id).get()
    available_qty=HostelRoomStudent.objects.filter(hostel=hostel, room=id).count()
    return total.number_of_bed-available_qty