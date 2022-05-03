from django.shortcuts import render, redirect
from .models import Book


def index(request):
    return redirect('books')


def books_view(request):
    list_books = Book.objects.all()
    template = 'books/books_list.html'
    context = {
        'books': list_books
    }
    return render(request, template, context)


def show_book(request, pub_date):
    template = 'books/books_list.html'
    selected_book = Book.objects.filter(pub_date=pub_date)

    previous_date = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    next_date = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()

    context = {
        'books': selected_book,
        'previous_date': previous_date,
        'next_date': next_date,
    }
    return render(request, template, context)
