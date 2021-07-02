from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from .form import *
from django.contrib import messages
import mimetypes
# Create your views here.

class AuthorsView(View):
    def get(self,request):
        authors=Author.objects.all().order_by('-id')
        contex = {'authors':authors}
        return render(request, 'author/index.html',contex)
class AddAuthorView(View):
    def get(self,request):
        form = AuthorForm()
        context = {'form':form}
        return render(request, 'author/create.html',context)
    def post(self,request):
        if request.method=='POST':
            author=request.POST
            form = AuthorForm(request.POST) 
            if form.is_valid():
               author=form.save()
               messages.success(request,'Data store successfull',extra_tags='success')
               return redirect(reverse('library:authors'))
        
class EditAuthorView(View):
    def get(self,request, pk):
        author=Author.objects.get(id=pk)
        form = AuthorForm(instance=author)
        context={'form':form}
        return render(request, 'author/create.html',context)
    def post(self,request, pk):
        author=Author.objects.get(id=pk)
        if request.method=='POST':
            form = AuthorForm(request.POST, instance=author)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('library:authors'))

        
class DeleteAuthorView(View):
    def get(self,request,pk):
        author=Author.objects.get(id=pk)
        author.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:authors'))




#-----------------------publisher------------------------

class PublishersView(View):
    def get(self,request):
        publishers=Publisher.objects.all().order_by('-id')
        contex = {'publishers':publishers}
        return render(request, 'publisher/index.html',contex)

class AddPublisherView(View):
    def get(self,request):
        form = PublisherForm()
        context = {'form':form}
        return render(request, 'publisher/create.html',context)
    def post(self,request):
        if request.method=='POST':
            publisher=request.POST
            form = PublisherForm(request.POST) 
            if form.is_valid():
                publisher=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('library:publishers'))
    
class EditPublisherView(View):
    def get(self,request, pk):
        publisher=Publisher.objects.get(id=pk)
        form = PublisherForm(instance=publisher)
        context={'form':form}
        return render(request, 'publisher/create.html',context)
    def post(self,request, pk):
        publisher=Publisher.objects.get(id=pk)
        if request.method=='POST':
            form = PublisherForm(request.POST, instance=publisher)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('library:publishers'))

    
class DeletePublisherView(View):
    def get(self,request,pk):
        publisher=Publisher.objects.get(id=pk)
        publisher.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:publishers'))



#-----------------------subject------------------------

class SubjectsView(View):
    def get(self,request):
        subjects=Subject.objects.all().order_by('-id')
        contex = {'subjects':subjects}
        return render(request, 'subject/index.html',contex)
class AddSubjectView(View):
    def get(self,request):
        form = SubjectForm()
        context = {'form':form}
        return render(request, 'subject/create.html',context)
    def post(self,request):
        if request.method=='POST':
            subject=request.POST
            form = SubjectForm(request.POST) 
            if form.is_valid():
                subject=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('library:subjects'))
    
class EditSubjectView(View):
    def get(self,request, pk):
        subject=Subject.objects.get(id=pk)
        form = SubjectForm(instance=subject)
        context={'form':form}
        return render(request, 'subject/create.html',context)
    def post(self,request, pk):
        subject=Subject.objects.get(id=pk)
        if request.method=='POST':
            form = SubjectForm(request.POST, instance=subject)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('library:subjects'))

    
class DeleteSubjectView(View):
    def get(self,request,pk):
        subject=Subject.objects.get(id=pk)
        subject.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:subjects'))


#-----------------------book_language------------------------

class BookLanguagesView(View):
    def get(self,request):
        book_languages=BookLanguage.objects.all().order_by('-id')
        contex = {'book_languages':book_languages}
        return render(request, 'book_language/index.html',contex)
class AddBookLanguageView(View):
    def get(self,request):
        form = BookLanguageForm()
        context = {'form':form}
        return render(request, 'book_language/create.html',context)
    def post(self,request):
        if request.method=='POST':
            book_language=request.POST
            form = BookLanguageForm(request.POST) 
            if form.is_valid():
                book_language=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('library:book_languages'))
    
class EditBookLanguageView(View):
    def get(self,request, pk):
        book_language=BookLanguage.objects.get(id=pk)
        form = BookLanguageForm(instance=book_language)
        context={'form':form}
        return render(request, 'book_language/create.html',context)
    def post(self,request, pk):
        book_language=BookLanguage.objects.get(id=pk)
        if request.method=='POST':
            form = BookLanguageForm(request.POST, instance=book_language)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('library:book_languages'))

    
class DeleteBookLanguageView(View):
    def get(self,request,pk):
        book_language=BookLanguage.objects.get(id=pk)
        book_language.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:book_languages'))


#-----------------------rack------------------------

class RacksView(View):
    def get(self,request):
        racks=Rack.objects.all().order_by('number')
        contex = {'racks':racks}
        return render(request, 'rack/index.html',contex)

class AddRackView(View):
    def get(self,request):
        form = RackForm()
        context = {'form':form}
        return render(request, 'rack/create.html',context)
    def post(self,request):
        if request.method=='POST':
            rack=request.POST
            form = RackForm(request.POST) 
            if form.is_valid():
                rack=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('library:racks'))
        
class EditRackView(View):
    def get(self,request, pk):
        rack=Rack.objects.get(id=pk)
        form = RackForm(instance=rack)
        context={'form':form}
        return render(request, 'rack/create.html',context)
    def post(self,request, pk):
        rack=Rack.objects.get(id=pk)
        if request.method=='POST':
            form = RackForm(request.POST, instance=rack)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('library:racks'))

    
class DeleteRackView(View):
    def get(self,request,pk):
        rack=Rack.objects.get(id=pk)
        rack.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:racks'))



#-----------------------book------------------------

class BooksView(View):
    def get(self,request):
        books=Book.objects.all().order_by('-id')
        contex = {'books':books}
        return render(request, 'book/index.html',contex)
class DetailBookView(View):
    def get(self,request, pk):
        book=Book.objects.get(id=pk)
        issue_list=BookIssue.objects.filter(book=pk, status=0)
        context={'book':book, 'issue_list':issue_list}
        return render(request, 'book/view.html',context)

class AddBookView(View):
    def get(self,request):
        form = BookForm()
        context = {'form':form}
        return render(request, 'book/create.html',context)
    def post(self,request):
        if request.method=='POST':
            book=request.POST
            form = BookForm(request.POST, request.FILES) 
            if form.is_valid():
                book=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('library:books'))
    

class EditBookView(View):
    def get(self,request, pk):
        book=Book.objects.get(id=pk)
        form = BookForm(instance=book)
        context={'form':form}
        return render(request, 'book/create.html',context)
    def post(self,request, pk):
        book=Book.objects.get(id=pk)
        if request.method=='POST':
            form = BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('library:books'))

    

class DeleteBookView(View):
    def get(self,request, pk):
        book=Book.objects.get(id=pk)
        book.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:books'))


#-----------------------ebook------------------------

class EbooksView(View):
    def get(self,request):
        ebooks=EBook.objects.all().order_by('-id')
        contex = {'ebooks':ebooks}
        return render(request, 'ebook/index.html',contex)

class DetailEbookView(View):
    def get(self,request,pk):
        ebook=EBook.objects.get(id=pk)
        context={'ebook':ebook}
        return render(request, 'ebook/view.html',context)

class AddEbookView(View):
    def get(self,request):
        form = EBookForm()
        context = {'form':form}
        return render(request, 'ebook/create.html',context)
    def post(self,request):
        if request.method=='POST':
            ebook=request.POST
            form = EBookForm(request.POST, request.FILES) 
            if form.is_valid():
                ebook=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('library:ebooks'))
    

class EditEbookView(View):
    def get(self,request,pk):
        ebook=EBook.objects.get(id=pk)
        form = EBookForm(instance=ebook)
        context={'form':form}
        return render(request, 'ebook/create.html',context)
    def post(self,request,pk):
        ebook=EBook.objects.get(id=pk)
        if request.method=='POST':
            form = EBookForm(request.POST, request.FILES, instance=ebook)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('library:ebooks'))

    

class DeleteEbookView(View):
    def get(self,request,pk):
        ebook=EBook.objects.get(id=pk)
        ebook.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:ebooks'))

#-----------------------book issue------------------------

class BookIssuesView(View):
    def get(self,request):
        book_issues=BookIssue.objects.filter(status=0).order_by('-id')
        contex = {'book_issues':book_issues, 'title':'Issue Book'}
        return render(request, 'book_issue/index.html',contex)

class BookReturnView(View):
    def get(self,request):
        book_issues=BookIssue.objects.filter(status=1).order_by('-id')
        contex = {'book_issues':book_issues, 'title':'Return Book'}
        return render(request, 'book_issue/index.html',contex)

class DetailBookIssueView(View):
    def get(self,request, pk):
        book_issue=BookIssue.objects.get(id=pk)
        context={'book_issue':book_issue}
        return render(request, 'book_issue/view.html',context)

class AddBookIssueView(View):
    def get(self,request,pk):
        total_issue=BookIssue.objects.filter(book=pk, status=0).count()
        total_qty=Book.objects.filter(id=pk).get()
        if total_qty.qty > total_issue:
            print(total_qty)
        else:
            messages.success(request,'Insuficient quantity',extra_tags='error')
            return redirect('/book_list')
        form = BookIssueForm()
        context = {'form':form, 'book':pk}
        return render(request, 'book_issue/create.html',context)
    def post(self,request,pk):
        if request.method=='POST':
            book_issue=request.POST
            form = BookIssueForm(request.POST) 
            if form.is_valid():
                book_issue=form.save()
                messages.success(request,'Data store successfull',extra_tags='success')
                return redirect(reverse('library:book_issues'))
        

class EditBookIssueView(View):
    def get(self,request,pk):
        book_issue=BookIssue.objects.get(id=pk)
        form = BookIssueForm(instance=book_issue)
        context={'form':form,'book':book_issue.book.id}
        return render(request, 'book_issue/create.html',context)
    def post(self,request,pk):
        book_issue=BookIssue.objects.get(id=pk)
        if request.method=='POST':
            form = BookIssueForm(request.POST, instance=book_issue)
            if form.is_valid():
                form.save()
                messages.success(request,'Data update successfull',extra_tags='success')
                return redirect(reverse('library:book_issues'))

    

class BookMakeReturView(View):
    def get(self,request,pk):
        #book_issue=BookIssue.objects.get(id=pk)
        BookIssue.objects.filter(pk=pk).update(status=1)
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:book_issues'))

class DeleteBookIssueView(View):
    def get(self,request,pk):
        book_issue=BookIssue.objects.get(id=pk)
        book_issue.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect(reverse('library:book_issues'))