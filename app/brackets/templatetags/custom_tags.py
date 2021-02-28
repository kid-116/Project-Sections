from django import template


register = template.Library()


@register.filter(name='select_active')
def select_active(reqs):
    return reqs.filter(is_active=True)

