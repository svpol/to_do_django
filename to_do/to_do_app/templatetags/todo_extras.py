from ..models import Task
from django import template


register = template.Library()


@register.simple_tag
def task_number(request, task_id):
    pass




