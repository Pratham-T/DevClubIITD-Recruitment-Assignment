from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    #path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', views.registerView, name='register_url'),
    path('logout/', LogoutView.as_view(next_page='dashboard'), name='logout'),
]