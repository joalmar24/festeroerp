from django.db import models

class TipoSocio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Condicion(models.Model):
    tipo = models.ForeignKey(
        TipoSocio,
        on_delete=models.CASCADE,
        related_name='condiciones'
    )
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Socio(models.Model):
    numero_festero = models.IntegerField(unique=True,null=True, blank=True, verbose_name="Nº Festero")
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200, blank=True, default='')
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True)
    tipo = models.ForeignKey(TipoSocio, on_delete=models.PROTECT)
    condicion = models.ForeignKey(
        Condicion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fecha_alta = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True)  # activo / baja lógica
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
