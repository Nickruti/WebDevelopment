from django.shortcuts import render, redirect
from .models import DailyUpdate, Materials
from .forms import DailyUpdateForm
from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import DailyUpdateTable
from login_page.views import login_
# Create your views here.

def dailyUpdate_list(request):
    if not request.user.is_authenticated:
        return redirect(login_)
    table = DailyUpdateTable(DailyUpdate.objects.all())

    return render(request, "table.html", {
        "table": table
    })
    

def dailyUpdate(request):
    if not request.user.is_authenticated:
        return redirect(login_)
    form = DailyUpdateForm(request.POST)
    table = DailyUpdateTable(DailyUpdate.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    if request.method == 'POST':
        if form.is_valid():
            dailyupdate = DailyUpdate.objects.create(
                date = form.cleaned_data["date"],
                total_workers = form.cleaned_data["total_workers"],
                male_coolie = form.cleaned_data["male_coolie"],
                female_coolie = form.cleaned_data["female_coolie"],
                mason = form.cleaned_data["mason"],
                centric_fitter = form.cleaned_data["centrinc_fitter"],
                materials_purchased = form.cleaned_data["materials_purchased"],
                material_details = form.cleaned_data["material_details"]
            ) 
            dailyupdate.save()
            form = DailyUpdateForm()


            return render(request, "dailyUpdate.html", {'form':form})
        else:
            form = DailyUpdateForm()

    return render(request, 'dailyUpdate.html', {'form':form})

