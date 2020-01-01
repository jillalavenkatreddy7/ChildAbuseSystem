from django.db import models
class ComplaintModel(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    complaint_sender_name=models.CharField(max_length=70)
    complaint_sender_place=models.CharField(max_length=70,default=True)
    complaint_sender_number=models.CharField(max_length=70)
    complaint_details=models.TextField()
    complainting_place=models.CharField(max_length=70,default=True)
    complaint_status=models.CharField(max_length=50)
    date_of_giving=models.DateTimeField(auto_now=True)
