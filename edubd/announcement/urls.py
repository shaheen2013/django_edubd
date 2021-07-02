from django.urls import path
from .views import notice, news, holiday
app_name = 'announcement'
urlpatterns = [
    #notice
    path('notices/',notice.NoticeView.as_view(), name="notices"),
    path('notice/<int:pk>',notice.DetailNoticeView.as_view(), name="notice"),
    path('add_notice/',notice.AddNoticeView.as_view(), name="add_notice"),
    path('edit_notice/<int:pk>',notice.EditNoticeView.as_view(), name="edit_notice"),
    path('delete_notice/<int:pk>',notice.DeleteNoticeView.as_view(), name="delete_notice"),
    
    #news
    path('news/',news.NewsView.as_view(), name="news"),
    path('news/<int:pk>',news.DetailNewsView.as_view(), name="news"),
    path('add_news/',news.AddNewsView.as_view(), name="add_news"),
    path('edit_news/<int:pk>',news.EditNewsView.as_view(), name="edit_news"),
    path('delete_news/<int:pk>',news.DeleteNewsView.as_view(), name="delete_news"),
    
    #holidays
    path('holidays/',holiday.HolidayView.as_view(), name="holidays"),
    path('holiday/<int:pk>',holiday.DetailHolidayView.as_view(), name="holiday"),
    path('add_holiday/',holiday.AddHolidayView.as_view(), name="add_holiday"),
    path('edit_holiday/<int:pk>',holiday.EditHolidayView.as_view(), name="edit_holiday"),
    path('delete_holiday/<int:pk>',holiday.DeleteHolidayView.as_view(), name="delete_holiday"),
   
]