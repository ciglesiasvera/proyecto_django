from django.urls import path
from . import views

urlpatterns = [
    path('listbook/', views.list_books, name='list_books'),
]
