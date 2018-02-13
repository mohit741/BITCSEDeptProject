from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegForm, UserForm
from .models import Profile


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/profile')
    else:
        return render(request, 'registration/login.html')


def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/profile', {'user': user})
    else:
        args = {'err': 'User credentials not valid!'}
        return render(request, 'registration/login.html', args)


def register_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        # form2 = RegForm(request.POST, instance=request.user.Profile)
        if user_form.is_valid():  # and form2.is_valid():
            user_form.save()
            # form2.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile')
    else:
        user_form = UserForm()
        # form2 = RegForm()
    return render(request, 'register.html', {'user_form': user_form})

    # if all((profile_form.is_valid(), address_form.is_valid())):
    #   profile = profile_form.save()
    #    address = address_form.save(commit=False)
    #   address.printer_profile = profile
    #  address.save()


def show_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('/login')


def logout_user(request):
    logout(request)
    return redirect('/login')
