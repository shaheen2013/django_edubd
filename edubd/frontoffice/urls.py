from django.urls import path
from .views import visitorbook, phonecalllog, postaldispatch, postalreceive, complain
app_name = 'frontoffice'
urlpatterns = [
    #visitor_book
    path('visitorbooks/',visitorbook.VisitorbookView.as_view(), name="visitorbooks"),
    path('visitorbook/<int:pk>',visitorbook.DetailVisitorbookView.as_view(), name="visitorbook"),
    path('add_visitorbook/',visitorbook.AddVisitorbookView.as_view(), name="add_visitorbook"),
    path('edit_visitorbook/<int:pk>',visitorbook.EditVisitorbookView.as_view(), name="edit_visitorbook"),
    path('delete_visitorbook/<int:pk>',visitorbook.DeleteVisitorbookView.as_view(), name="delete_visitorbook"),
    #ajax data
    path('get_user/',visitorbook.GetUserView.as_view(), name="get_user"),
    
    #phonecalllog
    path('phonecalllogs/',phonecalllog.PhonecalllogView.as_view(), name="phonecalllogs"),
    path('phonecalllog/<int:pk>',phonecalllog.DetailPhonecalllogView.as_view(), name="phonecalllog"),
    path('add_phonecalllog/',phonecalllog.AddPhonecalllogView.as_view(), name="add_phonecalllog"),
    path('edit_phonecalllog/<int:pk>',phonecalllog.EditPhonecalllogView.as_view(), name="edit_phonecalllog"),
    path('delete_phonecalllog/<int:pk>',phonecalllog.DeletePhonecalllogView.as_view(), name="delete_phonecalllog"),
    
    #postaldispatch
    path('postaldispatchs/',postaldispatch.PostaldispatchView.as_view(), name="postaldispatchs"),
    path('add_postaldispatch/',postaldispatch.AddPostaldispatchView.as_view(), name="add_postaldispatch"),
    path('edit_postaldispatch/<int:pk>',postaldispatch.EditPostaldispatchView.as_view(), name="edit_postaldispatch"),
    path('delete_postaldispatch/<int:pk>',postaldispatch.DeletePostaldispatchView.as_view(), name="delete_postaldispatch"),
    
    #postalreceive
    path('postalreceives/',postalreceive.PostalreceiveView.as_view(), name="postalreceives"),
    path('add_postalreceive/',postalreceive.AddPostalreceiveView.as_view(), name="add_postalreceive"),
    path('edit_postalreceive/<int:pk>',postalreceive.EditPostalreceiveView.as_view(), name="edit_postalreceive"),
    path('delete_postalreceive/<int:pk>',postalreceive.DeletePostalreceiveView.as_view(), name="delete_postalreceive"),
    
    #complain
    path('complains/',complain.ComplainView.as_view(), name="complains"),
    path('complain/<int:pk>',complain.DetailComplainView.as_view(), name="complain"),
    path('add_complain/',complain.AddComplainView.as_view(), name="add_complain"),
    path('edit_complain/<int:pk>',complain.EditComplainView.as_view(), name="edit_complain"),
    path('delete_complain/<int:pk>',complain.DeleteComplainView.as_view(), name="delete_complain"),
]