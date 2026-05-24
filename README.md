# Gestor Documental de Expedientes

Sistema web desarrollado con Python y Django para la administración, control e integración de expedientes relacionados con la entrega de tarjetas de programas de becas.

---

## Características principales

- Gestión completa de expedientes.
- Registro, edición y consulta de beneficiarios.
- Control de CURP e ID de tarjeta.
- Número de tarjeta bancaria como identificador operativo.
- Importación masiva de expedientes desde Excel.
- Actualización masiva de CURP desde Excel.
- Catálogos de municipios, localidades, escuelas y CABB's de atención.
- Dashboard administrativo con gráficas.
- Estadísticas por programa, municipio y estatus.
- Bitácora general de movimientos.
- Historial de cambios por expediente.
- Control de productividad por usuario.
- Exportación de reportes a Excel.
- Generación de PDF y carátulas.
- Sistema multiusuario con permisos.
- Diseño responsive para escritorio, tablet y celular.
- Respaldo de base de datos desde el panel administrativo.

---

## Tecnologías utilizadas

- Python
- Django
- MySQL / MariaDB
- Bootstrap 5
- Chart.js
- OpenPyXL
- xhtml2pdf
- HTML5
- CSS3
- JavaScript

---

## Instalación local

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO

2. Entrar a la carpeta del proyecto

cd gestor_documental/core

3. Crear entorno virtual

python -m venv env

4. Activar entorno virtual

.\env\Scripts\activate

5. Instalar dependencias

pip install -r requirements.txt

6. Ejecutar migraciones

python manage.py migrate

7. Ejecutar servidor local

python manage.py runserver

8. Abrir en navegador

http://127.0.0.1:8000/