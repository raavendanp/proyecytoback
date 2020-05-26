from django.db import models
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class Measure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Codigo = models.CharField(verbose_name='Codigo', max_length=20)
    Longitud = models.CharField(verbose_name='Longitud', max_length=3)
    Latitud = models.CharField(verbose_name='Latitud', max_length=3)
    Producto = models.CharField(verbose_name='Producto', max_length=20)
    Area = models.DecimalField(verbose_name='Area' ,decimal_places=2, max_digits=12, validators=[MinValueValidator(0.00)])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)