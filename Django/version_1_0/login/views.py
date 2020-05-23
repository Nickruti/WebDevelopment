from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Login
from add_sites.views import add_sites
from django.contrib import messages
# Create your views here.
def login_(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            try:
                Login.objects.get(username=username)
                Login.objects.get(password=password)
                
            except Login.DoesNotExist:
                messages.error(request,'Username or Password not correct!')
                return render(request, "login.html", {"form":form})
            return redirect(add_sites)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

def demo(request):
    return render(request, 'demo.html', {})
           
    
    
    