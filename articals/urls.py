from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='artical_index'),
    path('artical/create', views.artical_create, name='artical_create'),
    path('artical/create/post', views.artical_create_post, name='artical_create_post'),
    path('<int:artical_id>/', views.artical_detail, name='artical_detail'),

]