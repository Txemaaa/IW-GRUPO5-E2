from django.db import models

class Turno(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    area_trabajo = models.CharField(max_length=50)
    responsable = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)
    equipo = models.CharField(max_length=50)
    def __str__(self):
        return f"Turno {self.codigo} - {self.fecha} - {self.area_trabajo}"

class Parte_Trabajo(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    tarea = models.TextField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    incidencia = models.TextField(blank=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('completado', 'Completado')])
    def __str__(self):
        return f"Parte de Trabajo {self.codigo} - Turno {self.turno.codigo}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    puesto = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    codigo_empleado = models.CharField(max_length=10, unique=True)
    direccion = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
