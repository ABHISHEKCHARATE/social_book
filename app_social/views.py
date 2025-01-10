from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import SocialUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Book
from PyPDF2 import PdfReader
from django.core.mail import send_mail
from django.http import HttpResponse
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
        date_of_birth = request.POST.get('date_of_birth')


        
        if password == confirm_password:
            
            user = SocialUser(
                email=email,
                username=username,
                full_name=full_name,
                role=role,  
                city=city,
                state=state,
                date_of_birth=date_of_birth,
            )
            user.set_password(password)  
            user.save()

            
            login(request, user)

            
            return redirect('index')
        else:
            
            return render(request, 'register.html', {'error': 'Passwords do not match'})

    return render(request, 'register.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    return redirect('login') 
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



from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request): 
    try:
        send_mail(
            'Subject: Welcome to Django Email',
            'This is a test email from Django.',
            'charateabhishek3@gmail.com',  
            ['abhicharate02@gmail.com'], 
            fail_silently=False,
        )
        return HttpResponse('Email sent successfully!')
    except Exception as e:
        return HttpResponse(f'Error sending email: {e}')




# from django.http import JsonResponse
# from .models import Book

# def rest_book_view(request):
#     if request.method != 'GET':
#         return JsonResponse({"error": "Only GET method is allowed."}, status=405)
#     books = Book.objects.all()
#     books_data = []
#     for book in books:
#         books_data.append({
#             "title": book.title,
#             "author": book.author,
#             "description": book.description,
#             "genre": book.genre,
#             "created_at": book.created_at,
#             "updated_at": book.updated_at,
#             "extracted_text": book.extracted_text,
#             "file_url": book.file.url if book.file else None
#         })
#     return JsonResponse({"books": books_data})




# # views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework.authtoken.models import Token
# from .models import SocialUser
# from django.contrib.auth import authenticate

# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)

#         if user:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key})
#         return Response({"error": "Invalid credentials"}, status=400)


# def file_access(request, file_id):
#     book = get_object_or_404(Book, id=file_id)
    
    
#     if book.file:
#         return JsonResponse({
#             "file_url": book.file.url
#         })
#     else:
#         return JsonResponse({
#             "error": "File not found"
#         })