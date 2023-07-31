from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

from user.forms import MyUserCreationForm
from user.models import UserProfile

# Create your views here.


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            UserProfile.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'An error occured during registration')

    context = {'form': form}

    return render(request, 'user/signup.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is not correct')

    return render(request, 'user/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')
