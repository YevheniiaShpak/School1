from django import template
from registration.models import Teacher

register = template.Library()

@register.filter
def is_teacher(user):
    return Teacher.objects.filter(user=user).exists()

