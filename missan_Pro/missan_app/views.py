from django.shortcuts import render
from missan_app.missan_views import user_views
from missan_app.missan_views import driver_views
from missan_app.missan_views.driver_views import add_driver


def home(request):

    if request.user.is_authenticated:
        return render(request,'missan_app/home.html')
    else:
        return render(request,'missan_app/login.html')
