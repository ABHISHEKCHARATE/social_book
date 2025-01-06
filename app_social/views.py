from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')
