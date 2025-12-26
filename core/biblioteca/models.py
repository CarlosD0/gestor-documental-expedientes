from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    def __str__(self): return self.nombre
    class Meta: verbose_name_plural = "Categorías"

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self): return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    stock = models.PositiveIntegerField(default=1)
    disponible = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    def __str__(self): return f"{self.titulo} ({self.isbn})"

class Prestamo(models.Model):
    ESTADOS = [('P', 'Prestado'), ('D', 'Devuelto'), ('R', 'Retrasado')]
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion_estimada = models.DateField()
    fecha_devolucion_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
    renovaciones = models.PositiveIntegerField(default=0)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self): return f"Préstamo: {self.libro.titulo} - {self.usuario.username}"
    @property
    def esta_vencido(self):
        if self.estado == 'D': return False
        return self.fecha_devolucion_estimada < date.today()

class Reserva(models.Model):
    ESTADOS_RESERVA = [('P', 'Pendiente'), ('C', 'Completada'), ('X', 'Cancelada')]
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS_RESERVA, default='P')
    def __str__(self): return f"Reserva: {self.libro.titulo}"

# --- CONFIGURACIÓN GLOBAL ---
class Configuracion(models.Model):
    nombre_institucion = models.CharField(max_length=200, default="Biblioteca Central")
    tasa_multa_dia = models.DecimalField(max_digits=5, decimal_places=2, default=2.50, verbose_name="Costo Multa por Día")
    dias_prestamo_defecto = models.IntegerField(default=7, verbose_name="Días de Préstamo (Default)")
    moneda = models.CharField(max_length=5, default="S/.")
    
    def __str__(self): return "Configuración General"