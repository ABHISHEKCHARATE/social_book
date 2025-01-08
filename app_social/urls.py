from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('profile', views.user_profile, name='profile'),

    path('Author', views.Author_page, name='Author'),
    path('Sellers', views.Sellers_page, name='Sellers'),

    path('my-books/', views.my_books_page, name='my_books'),
    path('add-book/', views.add_book_page, name='add_book'),
    path('edit-book/<int:id>/', views.edit_book_page, name='edit_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),

    path('book', views.book_view, name='book'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)