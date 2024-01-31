from django.shortcuts import render, redirect
from .models import BandMember, Song
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.urls import reverse

def home(request):
    return render(request, 'myapp/home.html')

def members(request):
    members = BandMember.objects.all()
    return render(request, 'myapp/members.html', {'members': members})

def songs(request):
    songs = Song.objects.all()
    return render(request, 'myapp/songs.html', {'songs': songs})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('myapp:register'))
    else:
        form = UserRegistrationForm()

    return render(request, 'myapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home') 
    else:
        form = AuthenticationForm()

    return render(request, 'myapp/login.html', {'form': form})