from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import UserRegForm, UserLogForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile


def lk(request):
    return render(request, 'lk.html')


def user_register(request):
    form = UserRegForm()
    form2 = ProfileForm()
    if request.method == "POST":
        form2 = ProfileForm(request.POST)
        form = UserRegForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            user.profile.phone = form2.cleaned_data.get('phone')
            user.profile.course = form2.cleaned_data.get('course')
            user.profile.save()  
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка')
    return render(request, 'register.html', {'form': form, 'form2':form2})


def user_login(request):
    if request.method == "POST":
        form = UserLogForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLogForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
