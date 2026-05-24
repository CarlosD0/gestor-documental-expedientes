from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),

    # AJUSTES

    path(
        'ajustes/',
        views.ajustes_sistema,
        name='ajustes_sistema'
    ),

    # PRODUCTIVIDAD

    path(
        'productividad/',
        views.productividad,
        name='productividad'
    ),

    path(
        'mi-productividad/',
        views.mi_productividad,
        name='mi_productividad'
    ),

    # CARÁTULAS

    path(
        'caratulas/',
        views.caratulas,
        name='caratulas'
    ),

    path(
        'caratulas/pdf/',
        views.generar_caratula_pdf,
        name='generar_caratula_pdf'
    ),

    # MUNICIPIOS

    path(
        'municipios/',
        views.lista_municipios,
        name='lista_municipios'
    ),

    path(
        'municipios/nuevo/',
        views.registrar_municipio,
        name='registrar_municipio'
    ),

    # LOCALIDADES

    path(
        'localidades/',
        views.lista_localidades,
        name='lista_localidades'
    ),

    path(
        'localidades/nuevo/',
        views.registrar_localidad,
        name='registrar_localidad'
    ),

    path(
        'localidades/importar/',
        views.importar_localidades_excel,
        name='importar_localidades_excel'
    ),

    path(
        'localidades/por-municipio/<int:municipio_id>/',
        views.localidades_por_municipio,
        name='localidades_por_municipio'
    ),

    path(
        'escuelas/',
        views.lista_escuelas,
        name='lista_escuelas'
    ),

    path(
        'escuelas/importar/',
        views.importar_escuelas_excel,
        name='importar_escuelas_excel'
    ),

    path(
    'escuelas/detalle/<int:escuela_id>/',
    views.detalle_escuela_json,
    name='detalle_escuela_json'
    ),

    path(
    'escuelas/por-localidad/<int:localidad_id>/',
    views.escuelas_por_localidad,
    name='escuelas_por_localidad'
    ),

    path(
    'escuelas/estadisticas/',
    views.estadisticas_escuelas,
    name='estadisticas_escuelas'
    ),

    # EXPEDIENTES

    path(
        'expedientes/',
        views.lista_libros,
        name='lista_libros'
    ),

    path(
        'expedientes/detalle/<int:id>/',
        views.detalle_libro,
        name='detalle_libro'
    ),

    path(
        'expedientes/nuevo/',
        views.registrar_libro,
        name='registrar_libro'
    ),

    path(
        'expedientes/importar/',
        views.importar_libros_excel,
        name='importar_libros_excel'
    ),

    path(
        'expedientes/plantilla-excel/',
        views.descargar_plantilla_excel,
        name='descargar_plantilla_excel'
    ),

    path(
        'expedientes/editar/<int:id>/',
        views.editar_libro,
        name='editar_libro'
    ),

    path(
        'expedientes/estado/<int:id>/',
        views.activar_libro,
        name='activar_libro'
    ),

    path(
        'expedientes/eliminar/<int:id>/',
        views.eliminar_libro,
        name='eliminar_libro'
    ),

    path(
        'expedientes/entregar/<int:id>/',
        views.marcar_entregado,
        name='marcar_entregado'
    ),

    path(
        'expedientes/reporte-pdf/',
        views.reporte_libros_pdf,
        name='reporte_libros_pdf'
    ),

    path(
        'expedientes/exportar-excel/',
        views.exportar_libros_excel,
        name='exportar_libros_excel'
    ),

    path(
       'expedientes/importar-curps/',
       views.importar_curps_excel,
       name='importar_curps_excel'
    ),

    # RESPONSABLES

    path(
        'responsables/',
        views.lista_autores,
        name='lista_autores'
    ),

    path(
        'responsables/nuevo/',
        views.registrar_autor,
        name='registrar_autor'
    ),



    # USUARIOS

    path(
        'usuarios/',
        views.lista_usuarios,
        name='lista_usuarios'
    ),

    path(
        'usuarios/nuevo/',
        views.crear_usuario,
        name='crear_usuario'
    ),

    path(
        'usuarios/editar/<int:id>/',
        views.editar_usuario,
        name='editar_usuario'
    ),

    path(
        'usuarios/estado/<int:id>/',
        views.activar_usuario,
        name='activar_usuario'
    ),

    path(
      'cabbs/',
       views.lista_cabbs,
       name='lista_cabbs'
    ),

    path(
      'cabbs/nuevo/',
      views.registrar_cabb,
      name='registrar_cabb'
    ),

    path(
       'cabbs/editar/<int:id>/',
        views.editar_cabb,
       name='editar_cabb'
    ),
    
    #MOVIMIENTOS

    path(
       'bitacora/',
       views.bitacora_general,
       name='bitacora_general'
    ),

    # RESPALDOS

    path(
        'respaldos/',
        views.generar_respaldo_bd,
        name='generar_respaldo_bd'
    ),

    # PERFIL

    path(
        'perfil/',
        views.perfil,
        name='perfil'
    ),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

    

    