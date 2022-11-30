from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='artical'),
    path('<int:artical_id>/', views.artical_detail, name='artical_detail'),

]