from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import SocialUser
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
        # gender = request.POST.get('gender')
        city = request.POST.get('city')
        state = request.POST.get('state')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = SocialUser(
                email=email,
                username=username,
                full_name=full_name,
                # gender=gender,
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



def index(request):
    return render(request, 'index.html')