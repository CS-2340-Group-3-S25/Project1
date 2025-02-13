from django import template
register = template.Library()
@register.filter
def get_quantity(cart, movie_id):
    return cart.get(str(movie_id), 0)