from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import VitalReading
from .forms import VitalReadingForm


def dashboard(request):
    readings = VitalReading.objects.all()

    total_readings = readings.count()
    total_patients = readings.values('patient_id').distinct().count()
    latest = readings.order_by('-recorded_at').first()

    context = {
        'total_readings': total_readings,
        'total_patients': total_patients,
        'latest': latest,
    }

    return render(request, 'monitor/dashboard.html', context)


def readings(request):
    readings = VitalReading.objects.all().order_by('-recorded_at')

    return render(request, 'monitor/readings.html', {
        'readings': readings
    })


def add_reading(request):
    if request.method == 'POST':
        form = VitalReadingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('readings')
    else:
        form = VitalReadingForm()

    return render(request, 'monitor/add_reading.html', {
        'form': form
    })