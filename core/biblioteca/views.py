from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q, Count, Sum
from django.core.paginator import Paginator
from datetime import date, timedelta
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill

# Email imports
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import Libro, Prestamo, Autor, Categoria, Reserva, Configuracion
from .forms import (LibroForm, PrestamoForm, LectorForm, AutorForm, CategoriaForm, 
                    PerfilUpdateForm, ImportarLibrosForm, ConfiguracionForm)
from .utils import render_to_pdf

def es_bibliotecario(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

# --- HELPER: OBTENER CONFIGURACIÓN ---
def obtener_config():
    # Obtiene la configuración existente o crea una por defecto (ID=1)
    config, created = Configuracion.objects.get_or_create(id=1)
    return config

# --- ADMIN DE SISTEMA ---
@user_passes_test(es_bibliotecario)
def ajustes_sistema(request):
    config = obtener_config()
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST, instance=config)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Configuración actualizada correctamente!')
            return redirect('home')
    else:
        form = ConfiguracionForm(instance=config)
    return render(request, 'admin/configuracion.html', {'form': form})

# --- HOME ---
@login_required
def home(request):
    config = obtener_config()
    if request.user.is_staff:
        total_libros = Libro.objects.filter(activo=True).count()
        total_prestamos = Prestamo.objects.filter(estado='P').count()
        total_lectores = User.objects.count()
        total_vencidos = Prestamo.objects.filter(estado='P', fecha_devolucion_estimada__lt=date.today()).count()
        total_reservas = Reserva.objects.filter(estado='P').count()
        libros_recientes = Libro.objects.filter(activo=True).order_by('-id')[:5]
        
        datos_categorias = Libro.objects.filter(activo=True).values('categoria__nombre').annotate(cantidad=Count('id'))
        cat_labels = [item['categoria__nombre'] for item in datos_categorias if item['categoria__nombre']]
        cat_data = [item['cantidad'] for item in datos_categorias if item['categoria__nombre']]
        prestamos_devueltos = Prestamo.objects.filter(estado='D').count()
        prestamos_al_dia = total_prestamos - total_vencidos
        
        context = {
            'es_admin': True, 
            'total_libros': total_libros, 'total_prestamos': total_prestamos,
            'total_lectores': total_lectores, 'total_vencidos': total_vencidos, 'total_reservas': total_reservas,
            'libros_recientes': libros_recientes, 
            'cat_labels': cat_labels, 'cat_data': cat_data, 
            'prestamos_data': [prestamos_al_dia, total_vencidos, prestamos_devueltos],
            'config': config
        }
    else:
        mis_prestamos_activos = Prestamo.objects.filter(usuario=request.user, estado='P').count()
        mis_libros_leidos = Prestamo.objects.filter(usuario=request.user, estado='D').count()
        mis_reservas_count = Reserva.objects.filter(usuario=request.user, estado='P').count()
        novedades = Libro.objects.filter(activo=True).order_by('-id')[:4]
        
        context = {
            'es_admin': False, 
            'mis_prestamos_activos': mis_prestamos_activos, 
            'mis_libros_leidos': mis_libros_leidos, 'mis_reservas_count': mis_reservas_count, 
            'novedades': novedades
        }
    return render(request, 'home.html', context)

@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos actualizados')
            return redirect('perfil')
    else:
        form = PerfilUpdateForm(instance=request.user)
    return render(request, 'usuarios/perfil.html', {'form': form})

# --- LIBROS ---
@login_required
def lista_libros(request):
    busqueda = request.GET.get("buscar")
    libros_list = Libro.objects.filter(activo=True).order_by('titulo')
    
    if request.user.is_staff:
        libros_list = Libro.objects.all().order_by('titulo')
    
    if busqueda:
        libros_list = libros_list.filter(
            Q(titulo__icontains=busqueda) | 
            Q(autor__nombre__icontains=busqueda) | 
            Q(isbn__icontains=busqueda)
        ).distinct()
    
    paginator = Paginator(libros_list, 5) 
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'libros/lista_libros.html', {'page_obj': page_obj})

@login_required
def detalle_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    tiene_reserva = False
    if not request.user.is_staff:
        tiene_reserva = Reserva.objects.filter(libro=libro, usuario=request.user, estado='P').exists()
    relacionados = Libro.objects.filter(Q(categoria=libro.categoria) | Q(autor=libro.autor)).exclude(id=id).filter(activo=True).order_by('?')[:4]
    return render(request, 'libros/detalle_libro.html', {'libro': libro, 'relacionados': relacionados, 'tiene_reserva': tiene_reserva})

@user_passes_test(es_bibliotecario)
def registrar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro registrado')
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/form_libro.html', {'form': form, 'titulo': 'Registrar Libro'})

@user_passes_test(es_bibliotecario)
def editar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado')
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/form_libro.html', {'form': form, 'titulo': 'Editar Libro'})

@user_passes_test(es_bibliotecario)
def activar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    libro.activo = not libro.activo
    libro.save()
    if libro.activo:
        messages.success(request, 'Libro habilitado')
    else:
        messages.warning(request, 'Libro desactivado')
    return redirect('lista_libros')

@user_passes_test(es_bibliotecario)
def reporte_libros_pdf(request):
    config = obtener_config()
    libros = Libro.objects.filter(activo=True).order_by('titulo')
    data = {'libros': libros, 'fecha': timezone.now(), 'institucion': config.nombre_institucion}
    return render_to_pdf('libros/reporte_pdf.html', data)

# --- PRÉSTAMOS ---
@user_passes_test(es_bibliotecario)
def lista_prestamos(request):
    busqueda = request.GET.get("buscar")
    prestamos = Prestamo.objects.all().order_by('estado', '-fecha_prestamo')
    if busqueda:
        prestamos = prestamos.filter(
            Q(libro__titulo__icontains=busqueda) | 
            Q(usuario__username__icontains=busqueda) | 
            Q(usuario__first_name__icontains=busqueda)
        )
    return render(request, 'prestamos/lista_prestamos.html', {'prestamos': prestamos})

@user_passes_test(es_bibliotecario)
def registrar_prestamo(request):
    config = obtener_config()
    libro_id_inicial = request.GET.get('libro_id')
    libro_inicial = None
    if libro_id_inicial:
        libro_inicial = get_object_or_404(Libro, id=libro_id_inicial)

    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            usuario = prestamo.usuario
            libro = prestamo.libro
            
            prestamos_activos = Prestamo.objects.filter(usuario=usuario, estado='P')
            for p in prestamos_activos:
                if p.esta_vencido:
                    messages.error(request, f'Usuario {usuario.username} tiene morosidad.')
                    return render(request, 'prestamos/form_prestamo.html', {'form': form})
            
            if prestamos_activos.count() >= 3:
                messages.error(request, 'Límite de préstamos alcanzado.')
                return render(request, 'prestamos/form_prestamo.html', {'form': form})

            if libro.stock > 0:
                # Verificar reservas
                reserva = Reserva.objects.filter(libro=libro, usuario=usuario, estado='P').first()
                if reserva:
                    reserva.estado = 'C'
                    reserva.save()
                
                libro.stock -= 1
                if libro.stock == 0:
                    libro.disponible = False
                libro.save()
                prestamo.save()
                
                try:
                    html_message = render_to_string('emails/notificacion_prestamo.html', {'prestamo': prestamo})
                    send_mail(f"📚 Préstamo - {libro.titulo}", strip_tags(html_message), settings.EMAIL_HOST_USER, [usuario.email], html_message=html_message, fail_silently=True)
                    messages.success(request, 'Préstamo registrado.')
                except:
                    messages.warning(request, 'Registrado, pero falló el envío del correo.')
                return redirect('lista_prestamos')
            else:
                messages.error(request, 'No hay stock.')
    else:
        # Usamos los días de la configuración
        form = PrestamoForm(initial={'fecha_devolucion_estimada': date.today() + timedelta(days=config.dias_prestamo_defecto), 'libro': libro_inicial})
    return render(request, 'prestamos/form_prestamo.html', {'form': form})

@user_passes_test(es_bibliotecario)
def devolver_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)
    if prestamo.estado == 'D':
        return redirect('lista_prestamos')
    
    config = obtener_config()
    hoy = date.today()
    
    # Cálculo seguro de días
    dias_retraso = 0
    if hoy > prestamo.fecha_devolucion_estimada:
        dias_retraso = (hoy - prestamo.fecha_devolucion_estimada).days
    
    # Cálculo con tasa dinámica
    multa_calculada = dias_retraso * config.tasa_multa_dia

    if request.method == 'POST':
        prestamo.estado = 'D'
        prestamo.fecha_devolucion_real = hoy
        prestamo.multa = multa_calculada
        prestamo.save()
        
        libro = prestamo.libro
        libro.stock += 1
        libro.disponible = True
        libro.save()
        
        # Notificar reservas
        reservas = Reserva.objects.filter(libro=libro, estado='P').order_by('fecha_reserva')
        if reservas.exists():
            siguiente = reservas.first()
            try:
                html = render_to_string('emails/notificacion_disponible.html', {'reserva': siguiente})
                send_mail(f"🎉 Disponible {libro.titulo}", strip_tags(html), settings.EMAIL_HOST_USER, [siguiente.usuario.email], html_message=html, fail_silently=True)
                messages.info(request, f'Notificado a {siguiente.usuario.username}.')
            except:
                pass

        if multa_calculada > 0:
            messages.warning(request, f'Devolución con multa: {config.moneda} {multa_calculada:.2f}')
        else:
            messages.success(request, 'Devuelto a tiempo.')
        return redirect('lista_prestamos')

    return render(request, 'prestamos/confirmar_devolucion.html', {'prestamo': prestamo, 'hoy': hoy, 'dias_retraso': dias_retraso, 'multa': multa_calculada, 'costo_dia': config.tasa_multa_dia, 'moneda': config.moneda})

@login_required
def renovar_prestamo(request, id):
    prestamo = get_object_or_404(Prestamo, id=id)
    config = obtener_config()
    
    if request.user != prestamo.usuario and not request.user.is_staff:
        return redirect('home')
    
    if prestamo.estado != 'P':
        messages.error(request, "Solo activos.")
    elif prestamo.esta_vencido:
        messages.error(request, "Vencido.")
    elif prestamo.renovaciones >= 2:
        messages.warning(request, "Límite alcanzado.")
    elif Reserva.objects.filter(libro=prestamo.libro, estado='P').exists():
        messages.error(request, "No se puede renovar: Hay reservas.")
    else:
        # Renovación con días dinámicos
        prestamo.fecha_devolucion_estimada += timedelta(days=config.dias_prestamo_defecto)
        prestamo.renovaciones += 1
        prestamo.save()
        messages.success(request, f"Renovado hasta: {prestamo.fecha_devolucion_estimada}")
    
    if request.user.is_staff:
        return redirect('lista_prestamos')
    else:
        return redirect('mis_prestamos')

@login_required
def mis_prestamos(request):
    prestamos = Prestamo.objects.filter(usuario=request.user).order_by('estado', '-fecha_prestamo')
    return render(request, 'prestamos/mis_prestamos.html', {'prestamos': prestamos})

@login_required
def comprobante_prestamo(request, id):
    config = obtener_config()
    prestamo = get_object_or_404(Prestamo, id=id)
    if request.user != prestamo.usuario and not request.user.is_staff:
        return redirect('home')
    return render_to_pdf('prestamos/comprobante_pdf.html', {'prestamo': prestamo, 'fecha_impresion': timezone.now(), 'institucion': config.nombre_institucion})

# --- RESERVAS ---
@login_required
def reservar_libro(request, id):
    libro = get_object_or_404(Libro, id=id)
    if libro.stock > 0:
        messages.warning(request, "Tiene stock.")
        return redirect('detalle_libro', id=id)
    
    if Reserva.objects.filter(libro=libro, usuario=request.user, estado='P').exists():
        messages.warning(request, "Ya en lista.")
        return redirect('detalle_libro', id=id)
    
    Reserva.objects.create(libro=libro, usuario=request.user)
    messages.success(request, "¡En lista de espera!")
    return redirect('detalle_libro', id=id)

@login_required
def mis_reservas(request):
    return render(request, 'reservas/mis_reservas.html', {'reservas': Reserva.objects.filter(usuario=request.user).order_by('-fecha_reserva')})

@user_passes_test(es_bibliotecario)
def lista_reservas(request):
    return render(request, 'reservas/lista_reservas.html', {'reservas': Reserva.objects.filter(estado='P').order_by('libro', 'fecha_reserva')})

@login_required
def anular_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.user != reserva.usuario and not request.user.is_staff:
        return redirect('home')
    reserva.estado = 'X'
    reserva.save()
    messages.info(request, "Cancelada.")
    
    if request.user.is_staff:
        return redirect('lista_reservas')
    else:
        return redirect('mis_reservas')

# --- MOROSIDAD ---
@user_passes_test(es_bibliotecario)
def lista_morosos(request):
    config = obtener_config()
    hoy = date.today()
    morosos = Prestamo.objects.filter(estado='P', fecha_devolucion_estimada__lt=hoy).order_by('fecha_devolucion_estimada')
    for p in morosos:
        p.dias_retraso_calc = (hoy - p.fecha_devolucion_estimada).days
        p.deuda_calc = p.dias_retraso_calc * config.tasa_multa_dia
    return render(request, 'prestamos/lista_morosos.html', {'morosos': morosos, 'precio_dia': config.tasa_multa_dia, 'moneda': config.moneda})

@user_passes_test(es_bibliotecario)
def enviar_recordatorio(request, id):
    config = obtener_config()
    prestamo = get_object_or_404(Prestamo, id=id)
    if not prestamo.esta_vencido:
        return redirect('lista_morosos')
    try:
        dias = (date.today() - prestamo.fecha_devolucion_estimada).days
        deuda = dias * config.tasa_multa_dia
        html = render_to_string('emails/recordatorio_vencido.html', {'prestamo': prestamo, 'dias_retraso': dias, 'deuda': deuda, 'moneda': config.moneda})
        send_mail(f"⚠️ URGENTE: Devolución - {prestamo.libro.titulo}", strip_tags(html), settings.EMAIL_HOST_USER, [prestamo.usuario.email], html_message=html, fail_silently=False)
        messages.success(request, 'Enviado.')
    except:
        messages.error(request, 'Error.')
    return redirect('lista_morosos')

# --- LECTORES ---
@user_passes_test(es_bibliotecario)
def lista_lectores(request):
    busqueda = request.GET.get("buscar")
    lectores = User.objects.all().order_by('username')
    if busqueda:
        lectores = lectores.filter(Q(username__icontains=busqueda) | Q(first_name__icontains=busqueda)).distinct()
    return render(request, 'lectores/lista_lectores.html', {'lectores': lectores})

@user_passes_test(es_bibliotecario)
def detalle_lector(request, id):
    lector = get_object_or_404(User, id=id)
    total_prestamos = Prestamo.objects.filter(usuario=lector).count()
    prestamos_activos = Prestamo.objects.filter(usuario=lector, estado='P').count()
    total_multas = Prestamo.objects.filter(usuario=lector).aggregate(Sum('multa'))['multa__sum'] or 0.00
    historial = Prestamo.objects.filter(usuario=lector).order_by('-fecha_prestamo')
    return render(request, 'lectores/detalle_lector.html', {'lector': lector, 'total_prestamos': total_prestamos, 'prestamos_activos': prestamos_activos, 'total_multas': total_multas, 'historial': historial})

@user_passes_test(es_bibliotecario)
def carnet_lector_pdf(request, id):
    config = obtener_config()
    lector = get_object_or_404(User, id=id)
    return render_to_pdf('lectores/carnet_pdf.html', {'lector': lector, 'fecha_emision': timezone.now(), 'institucion': config.nombre_institucion})

@user_passes_test(es_bibliotecario)
def registrar_lector(request):
    if request.method == 'POST':
        form = LectorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lector registrado')
            return redirect('lista_lectores')
    else:
        form = LectorForm()
    return render(request, 'lectores/form_lector.html', {'form': form})

@user_passes_test(es_bibliotecario)
def activar_lector(request, id):
    lector = get_object_or_404(User, id=id)
    if not lector.is_superuser:
        lector.is_active = not lector.is_active
        lector.save()
        messages.success(request, 'Actualizado.')
    else:
        messages.error(request, 'No puedes tocar al Super Admin.')
    return redirect('lista_lectores')

# --- OTROS ---
@user_passes_test(es_bibliotecario)
def lista_autores(request):
    return render(request, 'autores/lista_autores.html', {'autores': Autor.objects.all().order_by('nombre')})

@user_passes_test(es_bibliotecario)
def registrar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrado')
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'autores/form_autor.html', {'form': form})

@user_passes_test(es_bibliotecario)
def lista_categorias(request):
    return render(request, 'categorias/lista_categorias.html', {'categorias': Categoria.objects.all().order_by('nombre')})

@user_passes_test(es_bibliotecario)
def registrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrada')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/form_categoria.html', {'form': form})

@user_passes_test(es_bibliotecario)
def exportar_libros_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inventario"
    ws.append(["ID", "ISBN", "Título", "Autor", "Categoría", "Stock", "Estado"])
    for l in Libro.objects.all():
        ws.append([l.id, l.isbn, l.titulo, l.autor.nombre, str(l.categoria), l.stock, "Activo" if l.activo else "Inactivo"])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Libros.xlsx"'
    wb.save(response)
    return response

@user_passes_test(es_bibliotecario)
def exportar_prestamos_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Préstamos"
    ws.append(["Libro", "Usuario", "F. Préstamo", "F. Estimada", "F. Real", "Estado", "Multa"])
    for p in Prestamo.objects.all():
        ws.append([p.libro.titulo, p.usuario.username, p.fecha_prestamo, p.fecha_devolucion_estimada, str(p.fecha_devolucion_real), p.get_estado_display(), p.multa])
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Prestamos.xlsx"'
    wb.save(response)
    return response

@user_passes_test(es_bibliotecario)
def importar_libros_excel(request):
    if request.method == 'POST':
        form = ImportarLibrosForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                wb = openpyxl.load_workbook(request.FILES['archivo_excel'])
                ws = wb.active
                cnt = 0
                for row in ws.iter_rows(min_row=2, values_only=True):
                    titulo, autor_n, cat_n, isbn, stock, desc = row
                    if not titulo or not isbn:
                        continue
                    autor, _ = Autor.objects.get_or_create(nombre=autor_n)
                    cat = None
                    if cat_n:
                        cat, _ = Categoria.objects.get_or_create(nombre=cat_n)
                    if not Libro.objects.filter(isbn=isbn).exists():
                        Libro.objects.create(titulo=titulo, autor=autor, categoria=cat, isbn=str(isbn), stock=stock or 1, descripcion=desc or "", activo=True, disponible=True)
                        cnt += 1
                messages.success(request, f'{cnt} libros importados.')
                return redirect('lista_libros')
            except Exception as e:
                messages.error(request, f'Error: {e}')
    else:
        form = ImportarLibrosForm()
    return render(request, 'libros/importar_libros.html', {'form': form})