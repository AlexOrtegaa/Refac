from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
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
            messages.error(request, 'Usuario no existente')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Contraseño o usuario incorrecto')


    return render(request, 'users/login_register.html', context)

def logoutUser(request):
    logout(request)
    messages.error(request, 'Correcto cierre de sesión')
    return redirect('login')
from django.views.decorators.csrf import csrf_exempt


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()


    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, '¡Cuenta creada!')
            
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, 'Ocurrió un error durante el registro.')

    context = {'page':page, 'form': form}
    return render(request, 'users/login_register.html', context)