from django.urls import path
from .views import type, leave
app_name = 'leave'

urlpatterns = [
    #type
    path('types/',type.TypeView.as_view(), name="types"),
    path('edit_type/<int:pk>',type.EditTypeView.as_view(), name="edit_type"),
    path('delete_type/<int:pk>',type.DeleteTypeView.as_view(), name="delete_type"), 
    
    #leave
    path('list/',leave.LeaveView.as_view(), name="list"),
    path('add/',leave.AddLeaveView.as_view(), name="add"),
    path('edit/<int:pk>',leave.EditLeaveView.as_view(), name="edit"),
    path('delete/<int:pk>',leave.DeleteLeaveView.as_view(), name="delete"), 
    path('approve/<int:pk>',leave.ApprovLeaveView.as_view(), name="approve"),
    path('decline/<int:pk>',leave.DeclineLeaveView.as_view(), name="decline"),
    
    
    
]