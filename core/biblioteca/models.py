from django.db import models
from django.contrib.auth.models import User


class Autor(models.Model):

    nombre = models.CharField(max_length=100)

    nacionalidad = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    cupo = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        verbose_name="Cupo asignado"
    )

    municipio_asignado = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Municipio Asignado"
    )

    cargo = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    telefono = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.municipio_asignado or 'Sin municipio'}"


class Municipio(models.Model):

    clave = models.CharField(
        max_length=10,
        unique=True
    )

    nombre = models.CharField(
        max_length=150
    )

    estado = models.CharField(
        max_length=150,
        default="VERACRUZ"
    )

    clave_estado = models.CharField(
        max_length=5,
        default="30"
    )

    def __str__(self):
        return f"{self.clave} - {self.nombre}"
    

class CABB(models.Model):

    clave = models.CharField(
        max_length=20,
        unique=True
    )

    nombre = models.CharField(
        max_length=150
    )

    responsable = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    foto = models.ImageField(
        upload_to='cabbs/',
        blank=True,
        null=True
    )

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):

        return f"{self.clave} - {self.nombre}"


class Localidad(models.Model):

    municipio = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        related_name='localidades'
    )

    clave = models.CharField(
        max_length=10
    )

    nombre = models.CharField(
        max_length=150
    )

    cabb = models.ForeignKey(
       CABB,
       on_delete=models.SET_NULL,
       null=True,
       blank=True,
       related_name='localidades'
    )

    def __str__(self):
        return f"{self.clave} - {self.nombre}"


class Escuela(models.Model):

    NIVEL_CHOICES = [
        ('PREESCOLAR', 'Preescolar'),
        ('PRIMARIA', 'Primaria'),
        ('SECUNDARIA', 'Secundaria'),
        ('MEDIA_SUPERIOR', 'Media Superior'),
        ('SUPERIOR', 'Superior'),
        ('OTRO', 'Otro'),
    ]

    municipio = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        related_name='escuelas'
    )

    localidad = models.ForeignKey(
        Localidad,
        on_delete=models.CASCADE,
        related_name='escuelas'
    )

    cct = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="CCT"
    )

    nombre = models.CharField(
        max_length=250,
        verbose_name="Nombre de la Escuela"
    )

    nivel = models.CharField(
        max_length=30,
        choices=NIVEL_CHOICES,
        default='OTRO'
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.cct} - {self.nombre}"


    
class ProgramaBeca(models.Model):

    clave = models.CharField(
        max_length=30,
        unique=True
    )

    nombre = models.CharField(
        max_length=200
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre


class Libro(models.Model):


    ESTATUS_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('ENTREGADO', 'Entregado'),
    ]

    TIPO_CAPTURA_CHOICES = [
        ('OPERATIVA', 'Operativa'),
        ('HISTORICA', 'Histórica'),
    ]

    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre(s)"
    )

    apellido_paterno = models.CharField(
        max_length=150,
        verbose_name="Apellido Paterno"
    )

    apellido_materno = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Apellido Materno"
    )

    titulo = models.CharField(
        max_length=300,
        editable=False,
        blank=True,
        verbose_name="Nombre Completo"
    )

    autor = models.ForeignKey(
        Autor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Responsable"
    )

    curp = models.CharField(
       max_length=18,
       unique=True,
       blank=True,
       null=True,
       verbose_name="CURP",
       error_messages={
        'unique': 'Ya hay una tarjeta asociada con esta CURP.'
       }
    )

    id_tarjeta = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name="ID de Tarjeta",
        error_messages={
            'unique': 'Ya hay una tarjeta registrada con este ID.'
        }
    )

    numero_tarjeta_bancaria = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        db_index=True,
        verbose_name="Número de Tarjeta Bancaria"
    )


    cct_escuela = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="CCT de la Escuela"
    )

    nombre_escuela = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Nombre de la Escuela"
    )

    escuela = models.ForeignKey(
        Escuela,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Escuela / CCT"
    )


    programa_beca = models.ForeignKey(
       ProgramaBeca,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Programa/Beca",
        related_name="expedientes"
    )

    municipio = models.CharField(
        max_length=150
    )

    localidad = models.CharField(
        max_length=150
    )

    periodo_entrega = models.CharField(
        max_length=100
    )

    fecha_entrega = models.DateField(
        null=True,
        blank=True
    )

    cupo = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    portada = models.ImageField(
        upload_to='evidencias/',
        null=True,
        blank=True,
        verbose_name="Evidencia de Entrega"
    )

    estatus = models.CharField(
        max_length=20,
        choices=ESTATUS_CHOICES,
        default='PENDIENTE'
    )

    tipo_captura = models.CharField(
         max_length=20,
         choices=TIPO_CAPTURA_CHOICES,
         default='OPERATIVA',
         verbose_name="Tipo de Captura"
    )

    disponible = models.BooleanField(default=True)

    activo = models.BooleanField(default=True)

    capturado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='capturas_realizadas',
        verbose_name="Capturado por"
    )

    fecha_captura_entrega = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Fecha de Captura de Entrega"
    )

    def nombre_completo(self):

        nombres = [
            self.nombre,
            self.apellido_paterno,
            self.apellido_materno
        ]

        return " ".join(
            [n for n in nombres if n]
        )

    def save(self, *args, **kwargs):

        self.titulo = self.nombre_completo()

        super().save(*args, **kwargs)

        # OPTIMIZAR IMAGEN
        if self.portada:

            from PIL import Image

            img = Image.open(self.portada.path)

            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            max_size = (1200, 1200)

            img.thumbnail(max_size)

            img.save(
                self.portada.path,
                optimize=True,
                quality=70
            )

    def __str__(self):
        return f"{self.titulo} - {self.curp}"


class BitacoraMovimiento(models.Model):

    ACCIONES = (
        ('CREAR', 'Crear'),
        ('EDITAR', 'Editar'),
        ('IMPORTAR', 'Importar'),
        ('ENTREGAR', 'Entregar'),
        ('ELIMINAR', 'Eliminar'),
        ('ACTIVAR', 'Activar'),
        ('DESACTIVAR', 'Desactivar'),
        ('CURP', 'Actualizar CURP'),
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='movimientos'
    )

    accion = models.CharField(
        max_length=20,
        choices=ACCIONES
    )

    descripcion = models.TextField(
        blank=True,
        null=True
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ['-fecha']

        verbose_name = 'Movimiento'

        verbose_name_plural = 'Bitácora de Movimientos'

    def __str__(self):

        return f"{self.usuario} - {self.accion}"



class Configuracion(models.Model):

    nombre_institucion = models.CharField(
        max_length=200,
        default="Coordinación Nacional de Becas para el Bienestar"
    )

    nombre_sare = models.CharField(
        max_length=200,
        default="SARE 3011 PAPANTLA"
    )

    municipio_sede = models.CharField(
        max_length=150,
        default="PAPANTLA"
    )

    responsable_operativo = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    cargo_responsable = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    logo_institucional = models.ImageField(
        upload_to='configuracion/',
        null=True,
        blank=True
    )

    color_principal = models.CharField(
        max_length=20,
        default="#0d6efd"
    )

    color_secundario = models.CharField(
        max_length=20,
        default="#198754"
    )

    mostrar_ranking_productividad = models.BooleanField(
        default=True
    )

    meta_diaria_entregas = models.PositiveIntegerField(
        default=100
    )

    obligar_evidencia_entrega = models.BooleanField(
        default=True
    )

    mensaje_bienvenida = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return "Configuración General"