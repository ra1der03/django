from django.db.models import Model
from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(max_length=100)
    price = models.IntegerField()
    release_date = models.DateField(max_length=10)
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)

