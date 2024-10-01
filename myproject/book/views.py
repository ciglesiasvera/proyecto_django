from django.shortcuts import render
from .models import Book

def list_books(request):
    # Libros con valoración mayor a 1500
    high_rating_books = Book.objects.filter(rating__gt=1500)

    # Todos los libros
    all_books = Book.objects.all()

    context = {
        'high_rating_books': high_rating_books,
        'all_books': all_books
    }

    return render(request, 'listbook.html', context)
