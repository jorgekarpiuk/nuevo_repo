from django.db import models

# Create your models here.
class Kiosco(models.Model):
    
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()

class Libreria(models.Model):
    
    producto = models.CharField(max_length=40)
    precio = models.IntegerField()

class Servicios(models.Model):
    
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
      
    
       
    