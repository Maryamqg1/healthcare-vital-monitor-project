from django.contrib import admin

# Register your models here.

from .models import VitalReading


@admin.register(VitalReading)
class VitalReadingAdmin(admin.ModelAdmin):
    list_display = (
        'patient_id',
        'patient_name',
        'temperature',
        'heart_rate',
        'spo2',
        'blood_pressure',
        'recorded_at',
    )
    list_filter = ('recorded_at',)
    search_fields = ('patient_id', 'patient_name')