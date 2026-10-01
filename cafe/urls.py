from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('preorder/', views.preorder, name='preorder'),
    path('preorder/success/', views.preorder_success, name='preorder_success'),
]