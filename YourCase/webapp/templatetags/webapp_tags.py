from django import template


register = template.Library()


@register.inclusion_tag('webapp/post_card.html')
def post_card(post, user: bool):
    return {'post': post, 'user': user}


