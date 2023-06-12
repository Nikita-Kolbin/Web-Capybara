from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:post_id>/', post, name='post'),
    path('profile/<slug:username>/', profile, name='profile'),
    path('addpost/', AddPost.as_view(), name='add_post')
]
