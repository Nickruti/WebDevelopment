from django.shortcuts import render
from .models import AddSites
from .forms import AddSitesForm
# Create your views here.

def add_sites(request):
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

            return render(request, "addsite.html", {'form':form})
        else:
            form = AddSitesForm()

    return render(request, 'addsite.html', {'form':form})
