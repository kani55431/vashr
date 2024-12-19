import io
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict):
    """
    Render a Django template to a PDF.
    
    :param template_src: Path to the Django template.
    :param context_dict: Context to pass to the template.
    :return: A PDF document as a BytesIO object.
    """
    template = get_template(template_src)
    context = context_dict
    html = template.render(context)
    result = io.BytesIO()
    pdf = pisa.CreatePDF(io.StringIO(html), dest=result)
    if pdf.err:
        return None
    return result.getvalue()
