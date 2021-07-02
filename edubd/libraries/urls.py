from django.urls import path
from .views import *
from . import views
app_name = 'library'
urlpatterns = [
    #author
    path('authors/',views.AuthorsView.as_view(), name="authors"),
    path('add_author/',views.AddAuthorView.as_view(), name="add_author"),
    path('edit_author/<int:pk>',views.EditAuthorView.as_view(), name="edit_author"),
    path('delete_author/<int:pk>',views.DeleteAuthorView.as_view(), name="delete_author"),
    
    #publisher
    path('publishers/',views.PublishersView.as_view(), name="publishers"),
    path('add_publisher/',views.AddPublisherView.as_view(), name="add_publisher"),
    path('edit_publisher/<int:pk>',views.EditPublisherView.as_view(), name="edit_publisher"),
    path('delete_publisher/<int:pk>',views.DeletePublisherView.as_view(), name="delete_publisher"),


    #subject
    path('subjects/',views.SubjectsView.as_view(), name="subjects"),
    path('add_subject/',views.AddSubjectView.as_view(), name="add_subject"),
    path('edit_subject/<int:pk>',views.EditSubjectView.as_view(), name="edit_subject"),
    path('delete_subject/<int:pk>',views.DeleteSubjectView.as_view(), name="delete_subject"),


    #book_language
    path('book_languages/',views.BookLanguagesView.as_view(), name="book_languages"),
    path('add_book_language/',views.AddBookLanguageView.as_view(), name="add_book_language"),
    path('edit_book_language/<int:pk>',views.EditBookLanguageView.as_view(), name="edit_book_language"),
    path('delete_book_language/<int:pk>',views.DeleteBookLanguageView.as_view(), name="delete_book_language"),

    #rack
    path('racks/',views.RacksView.as_view(), name="racks"),
    path('add_rack/',views.AddRackView.as_view(), name="add_rack"),
    path('edit_rack/<int:pk>',views.EditRackView.as_view(), name="edit_rack"),
    path('delete_rack/<int:pk>',views.DeleteRackView.as_view(), name="delete_rack"),

    #book
    path('books/',views.BooksView.as_view(), name="books"),
    path('book/<int:pk>',views.DetailBookView.as_view(), name="book"),
    path('add_book/',views.AddBookView.as_view(), name="add_book"),
    path('edit_book/<int:pk>',views.EditBookView.as_view(), name="edit_book"),
    path('delete_book/<int:pk>',views.DeleteBookView.as_view(), name="delete_book"),

    #ebook
    path('ebooks/',views.EbooksView.as_view(), name="ebooks"),
    path('ebook/<int:pk>',views.DetailEbookView.as_view(), name="ebook"),
    path('add_ebook/',views.AddEbookView.as_view(), name="add_ebook"),
    path('edit_ebook/<int:pk>',views.EditEbookView.as_view(), name="edit_ebook"),
    path('delete_ebook/<int:pk>',views.DeleteEbookView.as_view(), name="delete_ebook"),

    #book_issue
    path('book_issues/',views.BookIssuesView.as_view(), name="book_issues"),
    path('book_returns',views.BookReturnView.as_view(), name="book_returns"),
    path('book_issue/<int:pk>',views.DetailBookIssueView.as_view(), name="book_issue"),
    path('add_book_issue/<int:pk>',views.AddBookIssueView.as_view(), name="add_book_issue"),
    path('edit_book_issue/<int:pk>',views.EditBookIssueView.as_view(), name="edit_book_issue"),
    path('delete_book_issue/<int:pk>',views.DeleteBookIssueView.as_view(), name="delete_book_issue"),
    path('book_make_return/<int:pk>',views.BookMakeReturView.as_view(), name="book_make_return_submit"),

    
]