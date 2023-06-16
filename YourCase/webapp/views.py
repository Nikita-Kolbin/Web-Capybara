from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import *
from .forms import *


def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'title': post.title,
        'post': post
    }
    return render(request, 'webapp/post.html', context=context)


class Home(ListView):
    model = Post
    template_name = 'webapp/index.html'
    context_object_name = 'posts'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        'user': user,
        'posts': Post.objects.filter(creator=user),
        'title': user.username
    }
    return render(request, 'webapp/profile.html', context=context)


# class AddPost(CreateView):
#     model = Post
#     form_class = AddPostForm
#     template_name = 'webapp/add_post.html'
#     success_url = reverse_lazy('home')


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()
            for image in images:
                Image.objects.create(
                    post=post,
                    image=image
                )
            return redirect("home")
    else:
        form = AddPostForm()

    return render(request, 'webapp/add_post.html', context={'form': form, 'title': 'Добавить пост'})


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'webapp/delete_post.html', context)
    elif request.method == 'POST':
        post.delete()
        return redirect('home')
