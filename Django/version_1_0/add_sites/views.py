from .models import AddSites
from .forms import AddSitesForm
from django.contrib import messages
from daily_update.views import dailyUpdate
from django.shortcuts import render, redirect
from login_page.views import login_
# Create your views here.

def add_sites(request):
    if not request.user.is_authenticated:
        return redirect(login_)
    form = AddSitesForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            site = AddSites.objects.create(
                name = form.cleaned_data["name"],
                location = form.cleaned_data["location"],
                description = form.cleaned_data["description"],
                start_date = form.cleaned_data["date"]
            ) 
            site.save()
            form = AddSitesForm()
            return redirect(dailyUpdate)
        else:
            form = AddSitesForm()

    return render(request, 'addsite.html', {'form':form})
