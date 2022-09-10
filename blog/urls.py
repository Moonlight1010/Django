from django.urls import path
from .views import home , about, services, contact, read, myform, update, pen, penread, delete_view, search

urlpatterns = [
    path('', home, name='blog-name'),
    path('about/', about, name='blog-about'),
    path('services/', services, name='blog-services'),
    path('contact/', contact, name='blog-contact'),
    path('read/<int:id>', read, name='blog-read'),
    path('myform/', myform, name='blog-myform'),
    path('update/<int:id>', update, name='blog-update'),
    path('pen/<int:id>', pen, name='blog-pen'),
    path('penread/<int:id>', penread, name='blog-penread'),
    path('delete/<int:id>', delete_view, name='blog-delete'),
    path('search/', search, name='search'),
]