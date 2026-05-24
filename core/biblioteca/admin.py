from django.contrib import admin

from .models import (
    Autor,
    Libro,
    Municipio,
    Localidad,
    Configuracion,
    ProgramaBeca,
    Escuela,
    CABB,
    PerfilUsuario
)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'nacionalidad'
    )

    search_fields = (
        'nombre',
    )


@admin.register(ProgramaBeca)
class ProgramaBecaAdmin(admin.ModelAdmin):

    list_display = (
        'clave',
        'nombre',
        'activo'
    )

    search_fields = (
        'clave',
        'nombre'
    )

    list_filter = (
        'activo',
    )


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):

    list_display = (
        'clave_estado',
        'estado',
        'clave',
        'nombre'
    )

    search_fields = (
        'clave',
        'nombre'
    )

    list_filter = (
        'estado',
    )


@admin.register(CABB)
class CABBAdmin(admin.ModelAdmin):

    list_display = (
        'clave',
        'nombre',
        'responsable',
        'activo'
    )

    search_fields = (
        'clave',
        'nombre',
        'responsable'
    )

    list_filter = (
        'activo',
    )

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):

    list_display = (
        'municipio',
        'clave',
        'nombre'
    )

    search_fields = (
        'clave',
        'nombre',
        'municipio__nombre'
    )

    list_filter = (
        'municipio',
    )

@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):

    list_display = (
        'cct',
        'nombre',
        'nivel',
        'municipio',
        'localidad',
        'activo'
    )

    list_filter = (
        'nivel',
        'municipio',
        'activo'
    )

    search_fields = (
        'cct',
        'nombre'
    )


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'curp',
        'id_tarjeta',
        'programa_beca',
        'municipio',
        'localidad',
        'periodo_entrega',
        'estatus',
        'fecha_entrega',
        'capturado_por'
    )

    search_fields = (
        'titulo',
        'curp',
        'id_tarjeta',
        'cct_escuela',
        'nombre_escuela',
        'municipio',
        'localidad',
        'periodo_entrega'
    )

    list_filter = (
        'programa_beca',
        'estatus',
        'municipio',
        'periodo_entrega',
        'activo'
    )

    readonly_fields = (
        'titulo',
        'fecha_captura_entrega'
    )


@admin.register(Configuracion)
class ConfiguracionAdmin(admin.ModelAdmin):

    list_display = (
        'nombre_institucion',
        'nombre_sare',
        'municipio_sede',
        'meta_diaria_entregas'
    )


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):

    list_display = (
        'usuario',
        'municipio_asignado',
        'cargo',
        'telefono',
        'activo'
    )

    search_fields = (
        'usuario__username',
        'municipio_asignado',
        'cargo'
    )