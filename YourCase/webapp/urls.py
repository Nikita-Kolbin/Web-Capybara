from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<int:category_id>/', category, name='category'),
    path('post/<int:post_id>/', post, name='post'),
    path('profile/<slug:username>/', profile, name='profile'),
    path('add_post/', add_post, name='add_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('edit_profile/<int:profile_id>/', EditProfile.as_view(), name='edit_profile')
]
