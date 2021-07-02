from django import forms
from django.forms import ModelForm
from .models import *
from django.forms.widgets import Select

class DriverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DriverForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Driver
        fields='__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows' : 5}),
            'driving_licence_validity': forms.DateInput(attrs={'type' : 'date'}),
        }

class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Vehicle
        fields='__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows' : 5}),
            'year_made': forms.DateInput(attrs={'type' : 'date'}),
        }

class StopageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StopageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Stopage
        fields='__all__'
        widgets = {
            'address': forms.Textarea(attrs={'rows' : 5}),
        }


class RouteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RouteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['start_point'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['end_point'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Route
        fields='__all__'


class ScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['route'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['vehicle'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['driver'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Schedule
        fields='__all__'

        widgets = {
            'start_time': forms.TimeInput(attrs={'type' : 'time'}),
            'end_time': forms.TimeInput(attrs={'type' : 'time'}),
        }
class ScheduleStopageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScheduleStopageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['schedule'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['stopage'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= ScheduleStopage
        fields='__all__'

        widgets = {
            'reach_time': forms.TimeInput(attrs={'type' : 'time'}),
            'leave_time': forms.TimeInput(attrs={'type' : 'time'}),
        }

class FareForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FareForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['start_stopage'].widget.attrs.update({'class': 'form-control select2'})
            self.fields['end_stopage'].widget.attrs.update({'class': 'form-control select2'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= Fare
        fields='__all__'
        


class CustomSelect(Select):
    def render_option(self, selected_choices, option_value, option_label):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = ''  # make it empty string like in else statement or refactor all that method
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html('<option value="{}"{}>{}</option>', option_value, selected_html, force_text(option_label))

class ScheduleMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScheduleMemberForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            self.fields['user'].widget.attrs.update({'class': 'form-control select2','multiple':'multiple'})
            visible.field.widget.attrs['placeholder'] = 'Enter text here ...'
    class Meta:
        model= ScheduleMember
        fields='__all__'
        