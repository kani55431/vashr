from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm


def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the home page after logout


#signup user
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page
    else:
        form = SignUpForm()
    return render(request, 'userloginsignup/register.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Redirect based on the user's department
                if user.has_role('masteruser'):
                    return redirect('audit_home')  # Redirect to the audit app view
                else:
                    return redirect('home')  # Redirect to the home page
    else:
        form = LoginForm()
    return render(request, 'userloginsignup/login.html', {'form': form})


# user login portal system#

def home(request):
    return render(request, 'userloginsignup/home.html', { })