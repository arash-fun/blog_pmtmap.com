# simple tags django
from django import template
from ..models import Category


register = template.Library()

@register.simple_tag
def title():
    return 'webloot'

# inclusion tags

# arash: inclustion tags help us to doesnot repeat 'category':Category.objects.filter(status=True) in view.py
@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        'category':Category.objects.filter(status=True)
    }