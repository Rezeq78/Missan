from django.urls import path,re_path
from missan_app.missan_views import user_views
from missan_app.missan_views import driver_views
from missan_app import views
from django.conf.urls import include

app_name = 'missan_app'

urlpatterns = [
        path('home',views.home,name='home'),
        path('driversersearch',driver_views.driver_search,name='driversersearch'),
        path('adddriver',driver_views.add_driver,name='add_driver'),
        path('user_login',user_views.user_login,'user_login'),
        path('adduser',user_views.register,name='register'),
        path('login',user_views.user_login,name='user_login'),
        path('logout',user_views.user_logout,name='logout'),
        re_path(r'$',user_views.user_login,name='user_login'),
]
