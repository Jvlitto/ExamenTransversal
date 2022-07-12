from django.db import models
from django.db.models import Model 

# Create your models here.
class Persona(models.Model):
    rut=models.CharField(primary_key = True, max_length=10)
    nombre=models.CharField(max_length=30)
    apellido_paterno=models.CharField(max_length=30)
    apellido_materno=models.CharField(max_length=30)
    edad=models.IntegerField()
    vacuna=models.CharField(max_length=30)
    fecha=models.CharField(max_length=30)

class Vacuna(models.Model):
    id=models.IntegerField(primary_key=True)
    marca=models.CharField(max_length=10)
    laboratorio=models.CharField(max_length=10)
    stock=models.IntegerField()
    fecha_elab=models.CharField(max_length=30)
    fecha_ven=models.CharField(max_length=30)