from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from .views import LoginView
# from .views import file_access

from .views import send_email
urlpatterns = [
    path('', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('profile', views.user_profile, name='profile'),

    path('Author', views.Author_page, name='Author'),
    path('Sellers', views.Sellers_page, name='Sellers'),

    path('my-books/', views.my_books_page, name='my_books'),
    path('add-book/', views.add_book_page, name='add_book'),
    path('edit-book/<int:id>/', views.edit_book_page, name='edit_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),

    path('book', views.book_view, name='book'),
    # path('book/', views.rest_book_view, name='book_view'),
    path('send-email/', send_email, name='send_email'), 


    # path('api1/loginn/', LoginView.as_view(), name='api1-loginn'),
    # path('api2/file/<int:file_id>/', views.file_access, name='api2-file-access'),

    

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# http://127.0.0.1:8000/api1/login/
# http://127.0.0.1:8000/books/book/
# http://127.0.0.1:8000/api2/file/2/
