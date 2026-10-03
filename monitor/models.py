from django.db import models

# Create your models here.


class VitalReading(models.Model):
    patient_id = models.CharField(max_length=20)
    patient_name = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    heart_rate = models.PositiveIntegerField()
    spo2 = models.PositiveIntegerField()
    blood_pressure = models.CharField(max_length=20)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_id} - {self.patient_name}"