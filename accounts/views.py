from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    # If method isn't post, render the normal register page
    if request.method != 'POST':
        return render(request, 'registration/register.html')
    
    # Create an account
    first = request.POST['first-name']
    last = request.POST['last-name']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    User.objects.create_user(username, email, password, first_name=first, last_name=last)

    # Authenticate and log in the user, then redirect to main page
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponseRedirect(reverse('todolistapp:index'))

def signin(request):
    # If method isn't post, render the normal login page
    if request.method != 'POST':
        return render(request, 'registration/signin.html')
    
    # Check that the username exists, then store that user in a variable
    try:
        username = request.POST["username"]
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        context = {'usernameError': True}
        return render(request, 'registration/signin.html', context)
    
    # Check that the passwords match
    password = request.POST['password']
    if not user.check_password(password):
        context = {'passwordError': True}
        return render(request, 'registration/signin.html', context)
    
    # Authenticate and log in the user, then redirect to main page
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return HttpResponseRedirect(reverse('todolistapp:index'))