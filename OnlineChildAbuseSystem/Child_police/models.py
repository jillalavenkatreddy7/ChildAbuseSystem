from django.db import models
class PoliceRegistrationModel(models.Model):
    police_station_id=models.CharField(primary_key=True,max_length=70)
    station_place=models.CharField(max_length=70)
    station_ci_name=models.CharField(max_length=70)
    mandal=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=70,unique=True)
    station_mail=models.EmailField()
    complete_address=models.TextField(default=True,)
    password=models.CharField(max_length=70)
    status=models.CharField(max_length=50,default=True)
    Date_of_join=models.DateField(auto_now=True)

