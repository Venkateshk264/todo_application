from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return JsonResponse({'success': 'User registered successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)
            return JsonResponse({'success': 'User logged in'})
        else:
            return JsonResponse({'error': 'Invalid credentials'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def logout(request):
    django_logout(request)
    return JsonResponse({'success': 'User logged out'})
