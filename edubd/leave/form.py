from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import Select

class TypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Type
        fields='__all__'
        

class LeaveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['leave_type'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Leave
        fields='__all__'
        widgets = {
                'reason': forms.Textarea(attrs={'rows' : 5}),
                'apply_date': forms.DateInput(attrs={'type' : 'date'}),
                'from_date': forms.DateInput(attrs={'type' : 'date'}),
                'to_date': forms.DateInput(attrs={'type' : 'date'}),
            }  