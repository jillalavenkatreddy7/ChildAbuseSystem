from django.db import models

class NGORegistrationModel(models.Model):
    ngo_id=models.CharField(primary_key=True,max_length=70)
    ngo_place=models.CharField(max_length=70)
    ngo_volunteer_name=models.CharField(max_length=70)
    mandal=models.CharField(max_length=50)
    District=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=70,unique=True)
    Ngo_mail=models.EmailField()
    complete_address=models.TextField(default=True,)
    password=models.CharField(max_length=70)
    status=models.CharField(max_length=50,default=True)
    Date_of_join=models.DateField(auto_now=True)
class NewsLettersModel(models.Model):
    letter_id=models.AutoField(primary_key=True)
    letter_file=models.FileField(upload_to="files/")
    sender_name = models.CharField(max_length=100)
    place=models.CharField(max_length=70)
    address=models.TextField()
    sender_mail=models.EmailField()
    contact_number=models.CharField(max_length=70)
    status=models.CharField(max_length=70)
    data_of_posting=models.DateTimeField(auto_now=True)
