from django import template
from ..models import Setting
register = template.Library()

@register.simple_tag()
def home_page_title():
    return Setting.objects.all()