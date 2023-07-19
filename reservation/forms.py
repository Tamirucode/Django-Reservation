from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from .models import Booking


class AvailabilityForm(forms.Form):
    
   
    date = forms.DateField(
        required=True, input_formats=["%Y-%m-%dT", "%Y-%m-%dT"], widget=forms.DateInput(attrs={'type': 'datet-local'}))
    time = forms.TimeField(
        required=True, input_formats=["%H:%M", "%H:%M%Z"], widget=forms.TimeInput(attrs={'type': 'time-local'}))
    
    def check_working_hours(self, start, end):
        
        time = self.cleaned_data.get('time')
        date = self.cleaned_data.get('date')
        # This ensures that  booking handle between start and end of working hours.
        if not(time < start and time > end):
            raise ValidationError(
                "Times beyond working hours, please enter value within working hours")
        else:
            return self.cleaned_data
