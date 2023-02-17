from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        passw1 = request.POST['password1']
        passw2 = request.POST['password2']
        # check for validity of inputs
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken,choose another.')
        elif len(fname) == 0 or len(lname) == 0 or len(username) == 0:
            messages.error(request, 'All fields are required.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken, choose another.')
        elif not username.isalnum() or not fname.isalnum() or not lname.isalnum():
            messages.error(request, 'Only alpha-numeric characters allowed.')
        elif passw1 != passw2:
            messages.error(request, 'Passwords do not match.')
        if reg_form.is_valid():
            #create user
            user = User.objects.create_user(username=username, email=email, first_name=fname, last_name=lname,password=passw1)
            user.set_password(passw1)
            # create a confirm email maessage here, to enable user to activate account and login
            user.save()
            messages.success(request, 'Account successfully created.')
            return render(request, 'account/register.html')
    return render(request, 'account/register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, mark_safe('Welcome ' + user.username))
                return redirect('meal:home')
            else:
                messages.error(request, 'Invalid credentials,try again.')
                return render(request, 'account/signin.html')
        else:
            messages.error(request, 'All fields are required.')
            return render(request, 'account/signin.html')
    return render(request, 'account/signin.html')


def logout_page(request):
    logout(request)
    return redirect('meal:home')