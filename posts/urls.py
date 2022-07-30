from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('like/', views.post_like, name='post_like'),
]