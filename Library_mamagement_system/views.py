from django.shortcuts import render
from django.db.models import Q
from management.models import Book

def home(request):
    books = Book.objects.all()
    value = request.GET.get('find', '')
    if value:
        books = books.filter(
            Q(title__icontains=value) | 
            Q(author__icontains=value) |
            Q(book_id__icontains=value)
        )
    return render(request, 'index.html', {'books': books, 'search_value': value})