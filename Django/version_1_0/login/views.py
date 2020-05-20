from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Login
# Create your views here.
def login_(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            try:
                user = Login.objects.get(username=username)

                pwd = Login.objects.get(password=password)
                return render(request,"demo.html",
                       {"user":user})
            except Login.DoesNotExist:
                return render(request, "login.html", {"form":form})
            #return redirect(demo)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})

def demo(request):
    return render(request, 'demo.html', {})
           
    
    
    