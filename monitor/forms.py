from django import forms
from .models import VitalReading


class VitalReadingForm(forms.ModelForm):
    class Meta:
        model = VitalReading
        fields = [
            'patient_id',
            'patient_name',
            'temperature',
            'heart_rate',
            'spo2',
            'blood_pressure',
        ]

    def clean_spo2(self):
        value = self.cleaned_data['spo2']

        if value > 100:
            raise forms.ValidationError('SpO₂ cannot exceed 100%.')
        if value < 0:
            raise forms.ValidationError('SpO₂ cannot be negative.')

        return value