from django.shortcuts import render
from missan_app.missan_forms.driver_forms import DriverInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import datetime
now = datetime.date.today()


def driver_search(request):

    return render(request,'missan_app/driversearch.html')


def add_driver(request):

    if request.method == 'POST':

        driver_form = DriverInfoForm(data=request.POST)

        iqama_expiry = request.POST.get('iqama_expiry_date')
        driver_license = request.POST.get('driver_license_expiry_date')

        expiry_date_iqama_driver_license = ""
        if str(iqama_expiry) < str(now) or str(driver_license) < str(now):
            expiry_date_iqama_driver_license = "الاوراق الثبوتية منتهية"

        if driver_form.is_valid() and str(iqama_expiry) > str(now) and str(driver_license) > str(now):
            driver = driver_form.save()
            driver.save()
            return HttpResponseRedirect('home')
        else:
            return render(request,'missan_app/adddriver.html',{'driver_form':driver_form,'expiry_date_iqama_driver_license':expiry_date_iqama_driver_license})
    else:
     return render(request,'missan_app/adddriver.html')
