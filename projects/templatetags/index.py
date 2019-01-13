from django import template
register = template.Library()

@register.filter
def index(List, i):
    if(len(List) > i):
        return List[int(i)]
    else:
        return None
@register.filter
def div(a, b):
    return int(a / b)

@register.filter
def mod(a, b):
    return int(a % b)

@register.filter
def count(List):
    return len(List)

@register.filter
def minus(a, b):
    return a - b