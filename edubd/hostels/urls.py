from django.urls import path
from .views import hostel_type, hostel, room_type, room, designation

urlpatterns = [
    #hostel type
    path('hostel_type_list',hostel_type.hostel_type, name="hostel_type.list"),
    path('hostel_type/edit/<int:pk>',hostel_type.hostel_type_edit, name="hostel_type.edit"),
    path('hostel_type/delete/<int:pk>',hostel_type.hostel_type_delete, name="hostel_type.delete"),
    
    #hostel
    path('hostel_list',hostel.hostel, name="hostel.list"),
    path('hostel/view/<int:pk>',hostel.hostel_view, name="hostel.view"),
    path('hostel/create',hostel.hostel_create, name="hostel.create"),
    path('hostel/edit/<int:pk>',hostel.hostel_edit, name="hostel.edit"),
    path('hostel/delete/<int:pk>',hostel.hostel_delete, name="hostel.delete"),
    #assingn hostel room
    path('hostel/room/<int:pk>',hostel.hostel_room, name="hostel.room"),
    path('hostel/add_room/<int:pk>',hostel.hostel_add_room, name="hostel.add_room"),
    path('hostel/room_delete/<int:pk>/<int:room>',hostel.hostel_room_delete, name="hostel.room_delete"),
    #assingn hostel room student
    path('hostel/student/<int:hostel>/<int:room>',hostel.student, name="hostel.student"),
    path('hostel/add_student/<int:pk>',hostel.add_student, name="hostel.add_student"),
    path('hostel/student_delete/<int:pk>',hostel.student_delete, name="hostel.student_delete"),

    #room type
    path('room_type_list',room_type.room_type, name="room_type.list"),
    path('room_type/edit/<int:pk>',room_type.room_type_edit, name="room_type.edit"),
    path('room_type/delete/<int:pk>',room_type.room_type_delete, name="room_type.delete"),
    

    #room
    path('room_list',room.room, name="room.list"),
    path('room/create',room.room_create, name="room.create"),
    path('room/edit/<int:pk>',room.room_edit, name="room.edit"),
    path('room/delete/<int:pk>',room.room_delete, name="room.delete"),

    #designation
    path('designation_list',designation.index, name="designation.list"),
    path('designation/edit/<int:pk>',designation.edit, name="designation.edit"),
    path('designation/delete/<int:pk>',designation.delete, name="designation.delete"),


    #assingn hostel staff
    path('hostel/staff/<int:hostel>',hostel.staff, name="hostel.staff"),
    path('hostel/add_staff/<int:pk>',hostel.add_staff, name="hostel.add_staff"),
    path('hostel/staff_delete/<int:pk>',hostel.staff_delete, name="hostel.staff_delete"),
]