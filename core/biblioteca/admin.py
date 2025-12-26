from django.contrib import admin
from .models import Autor, Categoria, Libro, Prestamo

# Configuración personalizada para el Panel Admin

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    # Columnas que se ven en la lista
    list_display = ('titulo', 'autor', 'categoria', 'isbn', 'stock', 'activo', 'disponible')
    # Campos por los que se puede buscar
    search_fields = ('titulo', 'isbn', 'autor__nombre')
    # Filtros laterales
    list_filter = ('categoria', 'activo', 'autor')
    # Editar campos directamente en la lista
    list_editable = ('stock', 'activo')

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('libro', 'usuario', 'fecha_prestamo', 'fecha_devolucion_estimada', 'estado', 'esta_vencido_visual')
    search_fields = ('libro__titulo', 'usuario__username', 'usuario__first_name')
    list_filter = ('estado', 'fecha_prestamo')
    
    # Función para mostrar si está vencido en el admin con un icono
    def esta_vencido_visual(self, obj):
        if obj.esta_vencido:
            return '⚠️ VENCIDO'
        return 'OK'
    esta_vencido_visual.short_description = 'Vencimiento'