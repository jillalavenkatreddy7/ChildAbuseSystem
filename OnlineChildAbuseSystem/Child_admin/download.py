from django.shortcuts import HttpResponse,render,redirect
from django.views.generic import View
import csv
from Child_user.models import ComplaintModel
class DownloadRegisterComplaints(View):
    def get(self,request):
        response=HttpResponse(content_type="text/csv")
        response['Content-Disposition']='attachment;filename="registered_complaints.csv"'
        write=csv.writer(response)
        write.writerow(["complaint_id","complaint_sender_name","complaint_sender_place","complaint_sender_number",
                        "complaint_details","complainting_place","complaint_status","date_of_giving"])
        cqs=ComplaintModel.objects.filter(complaint_status="registered")
        for x in cqs:
            write.writerow([x.complaint_id,x.complaint_sender_name,x.complaint_sender_place,
                            x.complaint_sender_number,x.complaint_details,x.complainting_place,x.complaint_status,x.date_of_giving])

        return response
class DownloadSolvedComplaints(View):
    def get(self,requset):
        response=HttpResponse(content_type="text/csv")
        response['Content-Disposition']='attachment;filename="solved_complaints.csv"'
        write=csv.writer(response)
        write.writerow(["complaint_id","complaint_sender_name","complaint_sender_place","complaint_sender_number",
                        "complaint_details","complainting_place","complaint_status","date_of_giving"])
        cqs=ComplaintModel.objects.filter(complaint_status="solved")
        for x in cqs:
            write.writerow([x.complaint_id,x.complaint_sender_name,x.complaint_sender_place,
                            x.complaint_sender_number,x.complaint_details,x.complainting_place,x.complaint_status,x.date_of_giving])

        return response