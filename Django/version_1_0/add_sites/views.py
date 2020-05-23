from django.shortcuts import render
from .models import AddSites
from .forms import AddSitesForm
from django.contrib import messages
# Create your views here.

def add_sites(request):
    form = AddSitesForm(request.POST)
    messages.error(request,'Login Successful!')
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

            return render(request, "addsite.html", {'form':form})
        else:
            form = AddSitesForm()

    return render(request, 'addsite.html', {'form':form})
