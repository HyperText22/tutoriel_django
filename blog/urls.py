from django.urls import path
from . import views

urlpatterns = [
    path('all', views.get_all_post, name='post.all'),
]
