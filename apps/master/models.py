from django.db import models

# Create your models here.

class Habitacion(models.Model):
    descripcionHabitacion = models.CharField(max_length=50)

class Perfil(models.Model):
    nombrePerfil = models.CharField(max_length=50)

class Area(models.Model):
    nombreArea = models.CharField(max_length=50)

class Residente(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechaNacimiento = models.DateField()
    habitacion = models.ForeignKey(Habitacion, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)

class Colaborador(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True)
    fechaNacimiento = models.DateField()
    fechaIngreso = models.DateField(auto_now_add=True)
    fechaFin = models.DateField(null = True, blank=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)

class Aportador(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    numeroTarjeta = models.IntegerField(null=True, blank=True)
    fechaCreacion = models.DateField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)

    def __str__(self):
        return f'Rut: {self.rut} Clave: {self.password}'

class TipoAporte(models.Model):
    nombreTipo = models.CharField(max_length=50)

class Aporte(models.Model):
    montoAporte = models.IntegerField()
    fechaAporte = models.DateField(auto_now_add=True)
    aportador = models.ForeignKey(Aportador, on_delete=models.PROTECT)
    tipo = models.ForeignKey(TipoAporte, on_delete=models.PROTECT)

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50)

class Insumo(models.Model):
    nombreInsumo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

class StockInsumo(models.Model):
    cantidad = models.IntegerField()
    fechaStock = models.DateField(auto_now_add=True)
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT)

class Atencion(models.Model):
    fechaAtencion = models.DateField(auto_now_add=True)
    residente = models.ForeignKey(Residente, on_delete=models.PROTECT)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    insumo = models.ForeignKey(Insumo, on_delete=models.PROTECT)

class Notificacion(models.Model):
    aportador = models.ForeignKey(Aportador, on_delete=models.PROTECT)
    mensaje = models.CharField(max_length=255)
    fechaMensaje = models.DateField(auto_now_add=True)