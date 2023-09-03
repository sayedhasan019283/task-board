from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from project.models import ProjectModel


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('create_project')
    return render(request, 'accounts/register.html', {'form':form})

def profile(request):
    current_user = request.user
    if current_user.is_authenticated:
        projects = ProjectModel.objects.filter(user=current_user)
    return render(request, 'accounts/dashboard.html', {'data' : projects})

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('create_project')
        else:
            return render(request, 'accounts/signin.html')
    return render(request, 'accounts/signin.html')

def user_logout(request):
    logout(request)
    return redirect('register')