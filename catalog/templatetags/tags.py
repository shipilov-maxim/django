import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_time(format_string):
    dt_obj = datetime.datetime.now()
    return dt_obj.strftime(format_string)


@register.filter
def my_media(data):
    if data:
        return f'/media/{data}'
    return '/media/none.jpg'


@register.simple_tag
def media(data):
    if data:
        return f'/media/{data}'
    return '/media/none.jpg'


@register.filter
def string_slice(string: str):
    if len(string) > 200:
        return string[:200] + '...'
    return string

# Создание фильтра
# @register.filter(needs_autoescape=True)
# def initial_letter_filter(text, autoescape=True):
#     first, other = text[0], text[1:]
#     if autoescape:
#         esc = conditional_escape
#     else:
#         esc = lambda x: x
#     result = "<strong>%s</strong>%s" % (esc(first), esc(other))
#     return mark_safe(result)
