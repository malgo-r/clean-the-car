from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'baseauth/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'baseauth/signupuser.html', {'form': UserCreationForm()})

    # else create new user
    if request.POST['password1'] == request.POST['password2']:
        try:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
            login(request, user)
            return redirect('currenttodos')
        except IntegrityError:
            return render(request, 'baseauth/signupuser.html',
                          {'form': UserCreationForm(), 'error': "This user name has already been taken"})
    else:
        # tell user the passwords didnt match
        return render(request, 'baseauth/signupuser.html', {'form': UserCreationForm(), 'error': "Password didn't match"})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'baseauth/loginuser.html', {'form': AuthenticationForm()})
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request, 'baseauth/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
    login(request, user)
    return redirect('currenttodos')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def currenttodos(request):
    return render(request, 'baseauth/currenttodos.html')






