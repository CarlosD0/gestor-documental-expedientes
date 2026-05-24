from io import BytesIO
import os

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def link_callback(uri, rel):
    """
    Permite que xhtml2pdf encuentre archivos static y media.
    """

    if uri.startswith(settings.STATIC_URL):
        path = os.path.join(
            settings.BASE_DIR,
            'static',
           uri.replace(settings.STATIC_URL, '').replace('/', os.sep)
      )

    elif uri.startswith(settings.MEDIA_URL):
        path = os.path.join(
            settings.MEDIA_ROOT,
            uri.replace(settings.MEDIA_URL, '').replace('/', os.sep)
        )

    else:
        return uri

    if not os.path.isfile(path):
        raise Exception(f'Archivo no encontrado: {path}')

    return path


def render_to_pdf(template_src, context_dict=None):
    """
    Genera PDF a partir de una plantilla HTML.
    """

    if context_dict is None:
        context_dict = {}

    template = get_template(template_src)
    html = template.render(context_dict)

    result = BytesIO()

    pdf = pisa.pisaDocument(
        BytesIO(html.encode("UTF-8")),
        result,
        encoding='UTF-8',
        link_callback=link_callback
    )

    if not pdf.err:
        return HttpResponse(
            result.getvalue(),
            content_type='application/pdf'
        )

    return HttpResponse(
        'Error al generar PDF',
        status=500
    )