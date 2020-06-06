from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from sites.views import dashboard
from .forms import LoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def login_(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect(dashboard)
            else:
                messages.error(request,'Username or Password not correct!')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

def logout_(request):
	logout(request)
	return HttpResponseRedirect("/login")