from django.urls import path
from .views import driver, vehicle, stopage, route, schedule, fare
app_name = 'transport'

urlpatterns = [
    #driver
    path('drivers/',driver.DriversView.as_view(), name="drivers"),
    path('add_driver/',driver.AddDriverView.as_view(), name="add_driver"),
    path('edit_driver/<int:pk>',driver.EditDriverView.as_view(), name="edit_driver"),
    path('delete_driver/<int:pk>',driver.DeleteDriverView.as_view(), name="delete_driver"),
    
    
    #vehicle
    path('vehicles/',vehicle.VehiclesView.as_view(), name="vehicles"),
    path('add_vehicle/',vehicle.AddVehicleView.as_view(), name="add_vehicle"),
    path('edit_vehicle/<int:pk>',vehicle.EditVehicleView.as_view(), name="edit_vehicle"),
    path('delete_vehicle/<int:pk>',vehicle.DeleteVehicleView.as_view(), name="delete_vehicle"),
    #vehicles_driver
    path('vehicle_drivers/<int:pk>',vehicle.VehicleDriversView.as_view(), name="vehicle_drivers"),
    path('add_vehicle_driver/<int:pk>',vehicle.AddVehicleDriverView.as_view(), name="add_vehicle_driver"),
    path('delete_vehicle_driver/<int:vehicle>/<int:driver>',vehicle.DeleteVehicleDriverView.as_view(), name="delete_vehicle_driver_vehicle_driver"),
    #ajax
    path('get_driver',vehicle.GetDriverView.as_view(), name="get_driver"),

    #stopage
    path('stopages/',stopage.StopageView.as_view(), name="stopages"),
    path('add_stopage/',stopage.AddStopageView.as_view(), name="add_stopage"),
    path('edit_stopage/<int:pk>',stopage.EditStopageView.as_view(), name="edit_stopage"),
    path('delete_stopage/<int:pk>',stopage.DeleteStopageView.as_view(), name="delete_stopage"),
    
    
    #route
    path('routes/',route.RouteView.as_view(), name="routes"),
    path('add_route/',route.AddRouteView.as_view(), name="add_route"),
    path('edit_route/<int:pk>',route.EditRouteView.as_view(), name="edit_route"),
    path('delete_route/<int:pk>',route.DeleteRouteView.as_view(), name="delete_route"),
    
    #schedule
    path('schedules/',schedule.ScheduleView.as_view(), name="schedules"),
    path('add_schedule/',schedule.AddScheduleView.as_view(), name="add_schedule"),
    path('edit_schedule/<int:pk>',schedule.EditScheduleView.as_view(), name="edit_schedule"),
    path('delete_schedule/<int:pk>',schedule.DeleteScheduleView.as_view(), name="delete_schedule"),
    #schedule_stopage
    path('schedule_stopages/<int:pk>',schedule.ScheduleStopageView.as_view(), name="schedule_stopages"),
    path('add_schedule_stopage/<int:pk>',schedule.AddScheduleStopageView.as_view(), name="add_schedule_stopage"),
    path('delete_schedule_stopage/<int:pk>',schedule.DeleteScheduleStopageView.as_view(), name="delete_schedule_stopage"),
    #schedule_member
    path('schedule_members/<int:pk>',schedule.ScheduleMemberView.as_view(), name="schedule_members"),
    path('add_schedule_member/<int:pk>',schedule.AddScheduleMemberView.as_view(), name="add_schedule_member"),
    path('delete_schedule_member/<int:pk>',schedule.DeleteScheduleMemberView.as_view(), name="delete_schedule_member"),

    #fare
    path('fares/',fare.FareView.as_view(), name="fares"),
    path('add_fare/',fare.AddFareView.as_view(), name="add_fare"),
    path('edit_fare/<int:pk>',fare.EditFareView.as_view(), name="edit_fare"),
    path('delete_fare/<int:pk>',fare.DeleteFareView.as_view(), name="delete_fare"),
]