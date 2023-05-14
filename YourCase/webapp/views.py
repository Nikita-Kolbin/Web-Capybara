from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def post(request, post_id):
    context = {
        'title': 'пост',
        'post': Post.objects.get(pk=post_id)
    }
    return render(request, 'webapp/post.html', context=context)


class Home(ListView):
    model = Post
    template_name = 'webapp/index.html'
    context_object_name = 'posts'
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

