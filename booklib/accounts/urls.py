from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    #path('', views.indexView, name='home'),
    path('dashboard/', views.DashboardView.dashboard, name='dashboard'),
    path('return/<uuid:id>', views.DashboardView.returnBook, name = 'return'),
    path('accept/<uuid:id>', views.DashboardView.borrowRequestAccept, name='accept'),
    path('reject/<uuid:id>', views.DashboardView.borrowRequestReject, name='reject'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', views.registerView, name='register_url'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]