from django import template
from webapp.models import Image, Profile


register = template.Library()


@register.inclusion_tag('webapp/post_card.html')
def post_card(post, user: bool):
    return {'post': post, 'user': user}


@register.inclusion_tag('webapp/post_content.html')
def post_content(post, card: bool):
    images = Image.objects.filter(post=post)
    return {'post': post, 'images': images, 'card': card}


@register.inclusion_tag('webapp/user_link.html')
def user_link(user, post, card: bool):
    return {'user': user, 'post': post, 'card': card}

