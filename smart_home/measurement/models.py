from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)


class Measurement(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

