from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import Select


class NoticeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['notice_for'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Notice
        fields='__all__'
        widgets = {
                'description': forms.Textarea(attrs={'rows' : 5}),
                'active_date': forms.DateInput(attrs={'type' : 'date'}),
                
            }  

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['notice_for'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= News
        fields='__all__'
        widgets = {
                'description': forms.Textarea(attrs={'rows' : 5}),
                'active_date': forms.DateInput(attrs={'type' : 'date'}),
                
            } 
class HolidayForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HolidayForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Holiday
        fields='__all__'
        widgets = {
                'description': forms.Textarea(attrs={'rows' : 5}),
                'start_date': forms.DateInput(attrs={'type' : 'date'}),
                'end_date': forms.DateInput(attrs={'type' : 'date'}),
                
            } 