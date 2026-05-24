from django import forms
from django.contrib.auth.models import User

from .models import (
    Libro,
    Autor,
    PerfilUsuario,
    Configuracion,
    Municipio,
    Escuela,
    CABB,
    Localidad
)


# --- FORMULARIOS DE CATÁLOGO ---
class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor

        fields = [
            'nombre',
            'nacionalidad'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }



# NUEVO → MUNICIPIOS
class MunicipioForm(forms.ModelForm):

    class Meta:
        model = Municipio

        fields = [
            'clave_estado',
            'estado',
            'clave',
            'nombre'
        ]

        widgets = {

            'clave_estado': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'estado': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'clave': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


# NUEVO → LOCALIDADES
class LocalidadForm(forms.ModelForm):

    class Meta:
        model = Localidad

        fields = [
            'municipio',
            'clave',
            'nombre'
        ]

        widgets = {

            'municipio': forms.Select(attrs={
                'class': 'form-select'
            }),

            'clave': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

#CABBS
class CABBForm(forms.ModelForm):

    localidades = forms.ModelMultipleChoiceField(
        queryset=Localidad.objects.all().order_by(
            'municipio__nombre',
            'nombre'
        ),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        label='Localidades atendidas'
    )

    class Meta:
        model = CABB

        fields = [
            'clave',
            'nombre',
            'responsable',
            'foto',
            'descripcion',
            'activo'
        ]

        widgets = {
            'clave': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['localidades'].queryset = Localidad.objects.select_related(
            'municipio'
        ).order_by(
            'municipio__nombre',
            'nombre'
        )

        self.fields['localidades'].label_from_instance = (
           lambda obj:
           f"{obj.municipio.nombre} | {obj.nombre}"
        )

        if self.instance and self.instance.pk:

           self.fields['localidades'].initial = (
              self.instance.localidades.all()
            )

    def save(self, commit=True):

        cabb = super().save(commit=False)

        if commit:

            cabb.save()

            localidades = self.cleaned_data.get('localidades')

            Localidad.objects.filter(
                cabb=cabb
            ).update(
                cabb=None
            )

            if localidades:
                localidades.update(
                    cabb=cabb
                )

        return cabb

# --- FORMULARIO PRINCIPAL ---
class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro

        error_messages = {

            'curp': {
                'unique': 'Ya hay una tarjeta asociada con esta CURP.'
            },

            'id_tarjeta': {
                'unique': 'Ya hay una tarjeta registrada con este ID.'
            }

        }

        fields = [

            'nombre',
             'apellido_paterno',
             'apellido_materno',
            'curp',
            'id_tarjeta',
            'numero_tarjeta_bancaria',
            'programa_beca',

            'cupo',

            'cct_escuela',
            'nombre_escuela',
            'escuela',
            'municipio',
            'localidad',

            'periodo_entrega',

            'fecha_entrega',

            'descripcion',

            'portada',

            'activo'
        ]

        widgets = {

            'nombre': forms.TextInput(attrs={
             'class': 'form-control',
             'placeholder': 'Nombre(s)'
             }),

            'apellido_paterno': forms.TextInput(attrs={
             'class': 'form-control',
            'placeholder': 'Apellido paterno'
            }),

            'apellido_materno': forms.TextInput(attrs={
             'class': 'form-control',
             'placeholder': 'Apellido materno'
            }),

            'curp': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la CURP'
            }),

            'id_tarjeta': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID de tarjeta'
            }),

            'numero_tarjeta_bancaria': forms.TextInput(attrs={
                 'class': 'form-control',
                 'placeholder': 'Número de tarjeta bancaria'
            }),

            'programa_beca': forms.Select(attrs={
                'class': 'form-select'
            }),

            'cupo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: 308458'
            }),

            'cct_escuela': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CCT de la escuela',
                'readonly': 'readonly'
            }),

            'nombre_escuela': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la escuela',
                'readonly': 'readonly'
            }),
            'escuela': forms.HiddenInput(),

            'municipio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Municipio',
                'readonly': 'readonly'
            }),

            'localidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Localidad',
                'readonly': 'readonly'
            }),

            'periodo_entrega': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: Mayo-Agosto 2025'
            }),

            'fecha_entrega': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones adicionales'
            }),

            'portada': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['escuela'].queryset = Escuela.objects.none()

            if self.instance and self.instance.escuela:
              self.fields['escuela'].queryset = Escuela.objects.filter(
                 localidad=self.instance.escuela.localidad
              )


# --- FORMULARIO OPERATIVO ---
class EntregaOperativaForm(forms.ModelForm):

    class Meta:

        model = Libro

        fields = [

            'cupo',
            'fecha_entrega',
            'descripcion',
            'portada'

        ]

        widgets = {

            'cupo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el cupo'
            }),

            'fecha_entrega': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Observaciones'
            }),

            'portada': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


# --- GESTIÓN DE USUARIOS ---
class UsuarioOperativoForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='Contraseña'
    )
    cupo = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cupo asignado'
        }),
        label='Cupo'
    )

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'password'
        ]

        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Usuario'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre(s)'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellidos'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data['password']
        )

        # USUARIO OPERATIVO
        user.is_staff = False
        user.is_superuser = False

        if commit:

            user.save()

            perfil, created = PerfilUsuario.objects.get_or_create(
                usuario=user
            )

            perfil.cupo = self.cleaned_data.get('cupo')

            perfil.save()

        return user
    

class UsuarioEditarForm(forms.ModelForm):

    cupo = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cupo asignado'
        }),
        label='Cupo'
    )

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active'
        ]

        widgets = {

            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if self.instance and hasattr(self.instance, 'perfil'):
            self.fields['cupo'].initial = self.instance.perfil.cupo

    def save(self, commit=True):

        user = super().save(commit=False)

        if commit:

            user.save()

            perfil, created = PerfilUsuario.objects.get_or_create(
                usuario=user
            )

            perfil.cupo = self.cleaned_data.get('cupo')
            perfil.save()

        return user


class PerfilUpdateForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email'
        ]

        widgets = {

            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
        }


class ImportarLibrosForm(forms.Form):

    archivo_excel = forms.FileField(

        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx'
        })

    )

class ImportarLocalidadesForm(forms.Form):

    archivo_excel = forms.FileField(

        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx'
        })

    )


# --- CONFIGURACIÓN GLOBAL ---

class ConfiguracionForm(forms.ModelForm):

    class Meta:

        model = Configuracion

        fields = [

            'nombre_institucion',
            'nombre_sare',
            'municipio_sede',

            'responsable_operativo',
            'cargo_responsable',

            'logo_institucional',

            'color_principal',
            'color_secundario',

            'mostrar_ranking_productividad',
            'meta_diaria_entregas',

            'obligar_evidencia_entrega',

            'mensaje_bienvenida'
        ]

        widgets = {

            'nombre_institucion': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'nombre_sare': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'municipio_sede': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'responsable_operativo': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'cargo_responsable': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'logo_institucional': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),

            'color_principal': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color'
            }),

            'color_secundario': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color'
            }),

            'mostrar_ranking_productividad': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),

            'meta_diaria_entregas': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'obligar_evidencia_entrega': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),

            'mensaje_bienvenida': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }

#ESCUELAS

class EscuelaForm(forms.ModelForm):

    class Meta:
        model = Escuela

        fields = [
            'municipio',
            'localidad',
            'cct',
            'nombre',
            'nivel',
            'activo'
        ]

        widgets = {
            'municipio': forms.Select(attrs={'class': 'form-select'}),
            'localidad': forms.Select(attrs={'class': 'form-select'}),
            'cct': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.Select(attrs={'class': 'form-select'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ImportarEscuelasForm(forms.Form):

    archivo_excel = forms.FileField(
        label='Archivo Excel de escuelas',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )

class ImportarCurpForm(forms.Form):

    archivo_excel = forms.FileField(
        label='Archivo Excel de CURP',
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.xlsx'
        })
    )

