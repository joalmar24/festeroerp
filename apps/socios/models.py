from django.db import models

class Socio(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200, blank=True, default='')
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True)
    fecha_alta = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
