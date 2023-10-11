from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginUser(request):
    page= 'login'
    context = {'page':page}
    if request.user.is_authenticated:
        return redirect('index');

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            user = User.objects.get(username=username)
        except:
            print("Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print("Username or password is incorrect")


    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request, user)
            return redirect('index')

    context = {'page':page, 'form': form}
    return render(request, 'users/login_register.html', context)