from django import forms
from missan_app.missan_models.driver_models import DriverInfo
from django.db import models
from django.core import validators
import datetime
now = datetime.date.today()

def iqamaexpirydate(self):
    # check_in_date = datetime.datetime.strptime(self,"%Y-%m-%d").date()
    if str(self) <= str(now) :
        raise forms.ValidationError("الإقامة منتهية")
#
# def driverlicenseexpirydate(self):
#     # check_in_date = datetime.datetime.strptime(self,"%Y-%m-%d").date()
#     if str(self) <= str(now) :
#         raise forms.ValidationError("الرخصة منتهية")

# driverlicenseexpirydate('2020-03-03')

class DriverInfoForm(forms.ModelForm):

        class Meta():
            model = DriverInfo
            fields = '__all__'

            # iqama_number = forms.CharField(max_length=10)
            # first_name = forms.CharField(max_length=30)
            # second_name = forms.CharField(required = False,max_length=30)
            # fourth_name = forms.CharField(required = False,max_length=30)
            # last_name = forms.CharField(max_length=30)
            # joining_date = forms.DateField()
            # city = forms.CharField(max_length=30)
            # area = forms.CharField(max_length=30)
            # street = forms.CharField(max_length=30)
            # current_application = forms.CharField(required = False,max_length=50)
            # previous_application = forms.CharField(required = False,max_length=50)
            # iqama_expiry_date = models.DateField(validators=[iqamaexpirydate])
            # driver_license_expiry_date = forms.DateField()
            # sponsor_name = forms.CharField(max_length=100)
            # knows_aout_us = forms.CharField(required = False,max_length=200)
            # car_type = forms.CharField(max_length=30)
            # car_plate_number = forms.CharField(max_length=30)
            # car_color = forms.CharField(max_length=30)
            # car_model = forms.CharField(max_length=4)

            error_messages = {
                                'iqama_number':{
                                                'unique':"رقم السائق مسجل من قبل",
                                                'required':"رقم الإقامة إلزامي",
                                                'max_length':"رقم الهوية يجب ان يكون عشر ارقام",
                                                'iqamaexpirydate':"fasdsaf",
                                                },
                                'first_name':{
                                                'required':"الاسم الاول إلزامي",
                                                },
                                'last_name':{
                                                'required':"الإسم الأخير إلزامي",
                                                },
                                'joining_date':{
                                                'required':"تاريخ المباشرة إلزامي",
                                                },
                                'city':{
                                                'required':"يجب إدخال المدينة",
                                                },
                                'area':{
                                                'required':"يجب إدخال اسم الحي",
                                                },
                                'street':{
                                                'required':"يجب إدخال اسم الشارع",
                                                },
                                'iqama_expiry_date':{
                                                 'required':"يجب إدخال تاريخ إنتهاء الإقامة",
                                                 },
                                'driver_license_expiry_date':{
                                                'required':"يجب إدخال تاريخ إنتهاء الرخصة",
                                                 },
                                'sponsor_name':{
                                                'required':"يجب إدخال اسم الكفيل",
                                                },
                                'car_type':{
                                                'required':"يجب إدخال نوع السيارة",
                                                },
                                'car_plate_number':{
                                                'required':"يجب إدخال رقم اللوحة",
                                                },
                                'car_color':{
                                                'required':"يجب إدخال لون السيارة",
                                                },
                                'car_model':{
                                                'required':"يجب إدخال تاريخ صنع السيارة",
                                                'max_length':"موديل السيارة اربع خانات",
                                                },
                            }
