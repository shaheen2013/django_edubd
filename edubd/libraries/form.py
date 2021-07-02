from django import forms
from django.forms import ModelForm
from .models import *
from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField

class AuthorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Author
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }
        


#---------------------publisher------------------------------

class PublisherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublisherForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Publisher
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 2}),
        }



#---------------------subject------------------------------

class SubjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Subject
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }

#---------------------subject------------------------------

class SubjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Subject
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


#---------------------BookLanguage------------------------------

class BookLanguageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookLanguageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= BookLanguage
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
        }


#---------------------Rack------------------------------

class RackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Rack
        fields='__all__'
        

#---------------------book------------------------------

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            self.fields['author'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['publisher'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['book_language'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['rack'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['subject'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Book
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
            #'author': forms.Select(attrs={'class' : 'select2'})
        }

#---------------------e-book------------------------------
class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        html =  Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))

class EBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EBookForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
            self.fields['author'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['publisher'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['book_language'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['subject'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    image = ImageField(widget=PictureWidget)
    class Meta:
        model= EBook
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
            #'author': forms.Select(attrs={'class' : 'select2'})
        }




#---------------------Rack------------------------------

class BookIssueForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookIssueForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['member'].widget.attrs.update({'class': 'form-control select2'})
            #self.fields['issue_date'].widget.attrs.update({'class': 'form-control'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= BookIssue
        fields='__all__'

        widgets = {
            'note': forms.Textarea(attrs={'rows' : 5}),
            'issue_date': forms.DateInput(attrs={'type' : 'date'}),
            'return_date': forms.DateInput(attrs={'type' : 'date'}),
        }