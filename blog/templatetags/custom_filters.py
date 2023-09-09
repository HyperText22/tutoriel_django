from django import template

register = template.Library()

@register.filter
def mon_filtre_custom(valeur):
    return valeur[:4]