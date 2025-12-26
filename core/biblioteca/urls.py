from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ajustes/', views.ajustes_sistema, name='ajustes_sistema'), # NUEVO
    
    # LIBROS
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/detalle/<int:id>/', views.detalle_libro, name='detalle_libro'),
    path('libros/nuevo/', views.registrar_libro, name='registrar_libro'),
    path('libros/importar/', views.importar_libros_excel, name='importar_libros_excel'),
    path('libros/editar/<int:id>/', views.editar_libro, name='editar_libro'),
    path('libros/estado/<int:id>/', views.activar_libro, name='activar_libro'),
    path('libros/reporte-pdf/', views.reporte_libros_pdf, name='reporte_libros_pdf'),
    path('libros/exportar-excel/', views.exportar_libros_excel, name='exportar_libros_excel'),

    # PRÉSTAMOS
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('prestamos/nuevo/', views.registrar_prestamo, name='registrar_prestamo'),
    path('prestamos/devolver/<int:id>/', views.devolver_prestamo, name='devolver_prestamo'),
    path('prestamos/renovar/<int:id>/', views.renovar_prestamo, name='renovar_prestamo'),
    path('prestamos/exportar-excel/', views.exportar_prestamos_excel, name='exportar_prestamos_excel'),
    path('prestamos/comprobante/<int:id>/', views.comprobante_prestamo, name='comprobante_prestamo'),
    path('prestamos/morosos/', views.lista_morosos, name='lista_morosos'),
    path('prestamos/recordatorio/<int:id>/', views.enviar_recordatorio, name='enviar_recordatorio'),
    path('mis-prestamos/', views.mis_prestamos, name='mis_prestamos'),

    # RESERVAS
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/mis-reservas/', views.mis_reservas, name='mis_reservas'),
    path('reservas/crear/<int:id>/', views.reservar_libro, name='reservar_libro'),
    path('reservas/anular/<int:id>/', views.anular_reserva, name='anular_reserva'),

    # LECTORES
    path('lectores/', views.lista_lectores, name='lista_lectores'),
    path('lectores/detalle/<int:id>/', views.detalle_lector, name='detalle_lector'),
    path('lectores/carnet/<int:id>/', views.carnet_lector_pdf, name='carnet_lector_pdf'),
    path('lectores/nuevo/', views.registrar_lector, name='registrar_lector'),
    path('lectores/estado/<int:id>/', views.activar_lector, name='activar_lector'),

    # CATÁLOGOS
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/nuevo/', views.registrar_autor, name='registrar_autor'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nuevo/', views.registrar_categoria, name='registrar_categoria'),

    # PERFIL
    path('perfil/', views.perfil, name='perfil'),
]