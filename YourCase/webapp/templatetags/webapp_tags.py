from django import template
from webapp.models import Image, Profile


register = template.Library()


@register.inclusion_tag('webapp/post_card.html')
def post_card(post, request, user: bool):
    return {'post': post, 'request': request, 'user': user}


@register.inclusion_tag('webapp/post_content.html')
def post_content(post, card: bool):
    images = Image.objects.filter(post=post)
    return {'post': post, 'images': images, 'card': card}


@register.inclusion_tag('webapp/user_link.html')
def user_link(post, request, card: bool):
    return {'user': post.creator, 'post': post, 'request': request, 'card': card}

