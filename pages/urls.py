from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('go-vip', views.vip, name='go-vip'),
    path('success/', views.success_view, name='success'),
]