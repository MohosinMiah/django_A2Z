from django.urls import path

from . import views

urlpatterns = [
    path('/login', views.login_user, name='accounts_login'),
    path('/user/logout', views.logout_user, name='accounts_logout'),
  

]