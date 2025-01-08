from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import SocialUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Book
from PyPDF2 import PdfReader
import os

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('index')  
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        role = request.POST.get('role')  
        city = request.POST.get('city')
        state = request.POST.get('state')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        
        if password == confirm_password:
            
            user = SocialUser(
                email=email,
                username=username,
                full_name=full_name,
                role=role,  
                city=city,
                state=state
            )
            user.set_password(password)  
            user.save()

            
            login(request, user)

            
            return redirect('index')
        else:
            
            return render(request, 'register.html', {'error': 'Passwords do not match'})

    return render(request, 'register.html')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def Author_page(request):
    authors = SocialUser.objects.filter(role='Author',is_superuser=False)
    return render(request, 'Author.html',{'authors':authors})


@login_required
def Sellers_page(request):
    sellers = SocialUser.objects.filter(role='Seller',is_superuser=False)
    return render(request, 'Sellers.html',{'sellers':sellers})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def user_profile(request):
    
    user = request.user

   
    context = {
        'user': user,
    }

    return render(request, 'profile.html', context)




@login_required
def my_books_page(request):
    books = Book.objects.filter(user=request.user)
    
    if not books.exists():
        return redirect('add_book')  

   
    return render(request, 'my_books.html', {'books': books})



@login_required
def add_book_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST.get('author', request.user.username)
        description = request.POST['description']
        genre = request.POST['genre']
        file = request.FILES['file']
        

        book = Book.objects.create(
            user=request.user,
            title=title,
            author=author,
            description=description,
            genre=genre,
            file=file,
            
        )
        return redirect('my_books')
    default_author = request.user.username

    return render(request, 'add_book.html', {'default_author': default_author})

@login_required
def edit_book_page(request, id):
    book = get_object_or_404(Book, id=id, user=request.user)  

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.description = request.POST['description']
        book.genre = request.POST['genre']
        book.file = request.FILES['file'] if 'file' in request.FILES else book.file
        

        book.save()
        return redirect('my_books')  

    return render(request, 'edit_book.html', {'book': book})

@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id=id, user=request.user) 
    book.delete()  
    return redirect('my_books')  


def book_view(request):
    
    books = Book.objects.all()

    
    return render(request, 'book.html', {'books': books})




