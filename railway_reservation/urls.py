from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('train/<str:train_number>/', views.train_detail, name='train_detail'),
    path('train/<str:train_number>/book/', views.book_ticket, name='book_ticket'),
    path('register/', views.register, name='register'),
    path('train-search/', views.train_search, name='train_search'),
]
