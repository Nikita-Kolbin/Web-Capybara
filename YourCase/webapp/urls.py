from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:post_id>/', post, name='post'),
    path('profile/<slug:username>/', profile, name='profile'),
    path('add_post/', add_post, name='add_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post')
]
