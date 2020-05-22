from django.shortcuts import render
from .models import DailyUpdate, Materials
from .forms import DailyUpdateForm
# Create your views here.

def dailyUpdate(request):
    form = DailyUpdateForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            dailyupdate = DailyUpdate.objects.create(
                date = form.cleaned_data["date"],
                total_workers = form.cleaned_data["total_workers"],
                male_coolie = form.cleaned_data["male_coolie"],
                female_coolie = form.cleaned_data["female_coolie"],
                mason = form.cleaned_data["mason"],
                centric_fitter = form.cleaned_data["centric_fitter"],
                materials_purchased = form.cleaned_data["materials_purchased"],
                material_details = form.cleaned_data["material_details"]
            ) 
            dailyupdate.save()
            form = DailyUpdateForm()

            return render(request, "dailyUpdate.html", {'form':form})
        else:
            print("Hello")
            form = DailyUpdateForm()

    return render(request, 'dailyUpdate.html', {'form':form})