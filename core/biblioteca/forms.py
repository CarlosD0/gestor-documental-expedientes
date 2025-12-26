from django import forms
from django.contrib.auth.models import User
from .models import Libro, Prestamo, Autor, Categoria, Configuracion

# --- FORMULARIOS DE CATÁLOGO ---
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'nacionalidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'})
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2})
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'categoria', 'isbn', 'stock', 'descripcion', 'portada', 'disponible', 'activo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'portada': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# --- FORMULARIO DE PRÉSTAMO (MODIFICADO) ---
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'usuario', 'fecha_devolucion_estimada']
        widgets = {
            'libro': forms.Select(attrs={'class': 'form-select'}),
            'usuario': forms.Select(attrs={'class': 'form-select'}), # Aquí aplica el Select2
            'fecha_devolucion_estimada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 1. Libros: Mostrar Título y Stock disponible
        self.fields['libro'].queryset = Libro.objects.filter(activo=True)
        self.fields['libro'].label_from_instance = lambda obj: f"{obj.titulo} (Stock: {obj.stock})"
        
        # 2. Usuarios: Mostrar DNI y Nombre Completo para facilitar la búsqueda
        self.fields['usuario'].queryset = User.objects.filter(is_active=True).order_by('username')
        self.fields['usuario'].label_from_instance = lambda obj: f"{obj.username} | {obj.first_name} {obj.last_name}"

# --- GESTIÓN DE USUARIOS ---
class LectorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Contraseña")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI / Código'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ImportarLibrosForm(forms.Form):
    archivo_excel = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': '.xlsx'}))

# --- CONFIGURACIÓN GLOBAL ---
class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ['nombre_institucion', 'tasa_multa_dia', 'dias_prestamo_defecto', 'moneda']
        widgets = {
            'nombre_institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'tasa_multa_dia': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.10'}),
            'dias_prestamo_defecto': forms.NumberInput(attrs={'class': 'form-control'}),
            'moneda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: S/.'}),
        }