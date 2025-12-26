from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # name - это имя маршрута
    path('auf/', views.auf, name='auf'),
    path('reg/', views.reg, name='reg'),
]