from django.urls import path
from . import views

urlpatterns = [
    path('all', views.get_all_post, name='post.all'),
    path('post/<int:pk>', views.post, name='post.post'),
]
