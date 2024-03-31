from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter
@stringfilter
def convert_markdown(content):
    md = markdown.Markdown(
        extensions=["fenced_code", "codehilite"])
    return mark_safe(md.convert(content))
