from django.shortcuts import render, redirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import View, ListView,DeleteView,ArchiveIndexView
from Child_admin.models import AdminModel
from Child_police.models import PoliceRegistrationModel
from django.contrib import messages
from Child_admin import sms
from Child_NGOs.models import NGORegistrationModel,NewsLettersModel
from Child_user.models import ComplaintModel
import csv


class AdminHome(View):
    def get(self,request):
        try:
            uname=request.session["uname"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired.....!"})
        else:
            return render(request,"Admin_templates/admin_home.html")

class AdminCheck(View):
    def post(self, requset):
        uname = requset.POST.get("uname")
        pword = requset.POST.get("pword")
        try:
            AdminModel.objects.get(username=uname, password=pword)
            requset.session["uname"] = uname
        except AdminModel.DoesNotExist:
            return render(requset, "Admin_templates/adminlogin.html", {"data": "Invalid username or password"})
        else:
            return render(requset, "Admin_templates/admin_home.html")


class Logout(View):
    def get(self, request):
        try:
            del request.session["uname"]
        except:
            return render(request, 'Main_templates/main.html', {"data": "sucessfully logged out"})
        else:
            return render(request,'Main_templates/main.html',{"data":"sucessfully logged out"})


class Pendings(ListView):
    queryset = PoliceRegistrationModel.objects.filter(status="pending")
    template_name = "Admin_templates/pendings.html"
    context_object_name = "data"


class Approving(View):
    def get(self, requset):
        id = requset.GET.get("id")
        qs = PoliceRegistrationModel.objects.filter(police_station_id=id)
        qs.update(status="approved")
        # station_id = ''
        # station_contact = ''
        # station_password = ''
        # for x in qs:
        #     station_id = x.police_station_id
        #     station_contact = x.contact_number
        #     station_password = x.password
        # message = "we are approved your request, now you can login with your credentials station_id:" + station_id + "password:" + station_password
        # sms.sendSms(message, station_contact)
        messages.success(requset, "Sucessfully Approved")
        return redirect('pendings')


class Approved(ListView):
    queryset = PoliceRegistrationModel.objects.filter(status="approved")
    template_name = "Admin_templates/approved.html"
    context_object_name = "data"

class Remove(View):
    def get(self,requset,id):
        PoliceRegistrationModel.objects.get(police_station_id=id).delete()
        return redirect('pendings')

class Decline(View):
    def get(self,requset,id):
        qs=PoliceRegistrationModel.objects.filter(police_station_id=id)
        qs.update(status='declined')
        messages.success(requset, "Sucessfully Declined")
        return redirect('pendings')

class Declined_req(ListView):
    queryset = PoliceRegistrationModel.objects.filter(status="declined")
    template_name = "Admin_templates/declined.html"
    context_object_name = "data"

class PendingNGO(ListView):
    queryset = NGORegistrationModel.objects.filter(status="pending")
    template_name = "Admin_templates/ngo_pending.html"
    context_object_name = "data"
class NGOApprove(View):
    def get(self,requset):
        id=requset.GET.get("id")
        nqs=NGORegistrationModel.objects.filter(ngo_id=id)
        nqs.update(status="approved")
        # id = ''
        # contact = ''
        # password = ''
        # for x in nqs:
        #     id = x.ngo_id
        #     contact = x.contact_number
        #     password = x.password
        # message = "we are approved your request, now you can login with your credentials ngo_id:" +id+ "password:" + password
        # sms.sendSms(message, contact)
        messages.success(requset, "Sucessfully Approved")
        return redirect('pendingngo')

class ApprovedNGO(ListView):
    queryset = NGORegistrationModel.objects.filter(status="approved")
    template_name = "Admin_templates/ngoapproved.html"
    context_object_name = "data"

class DeclineNgo(View):
    def get(self,request):
        id=request.GET.get("id")
        nqs=NGORegistrationModel.objects.filter(ngo_id=id)
        nqs.update(status="declined")
        messages.success(request, "Sucessfully Declined")
        return redirect('pendingngo')

class NGORemove(View):
    def get(self,request):
        id=request.GET.get("id")
        NGORegistrationModel.objects.get(ngo_id=id).delete()
        return redirect('pendingngo')

class DeclineNGORequests(ListView):
    queryset = NGORegistrationModel.objects.filter(status="declined")
    template_name = "Admin_templates/ngodeclined.html"
    context_object_name = "data"

class PendinglettersData(ListView):
    queryset = NewsLettersModel.objects.filter(status="pending")
    template_name = "Admin_templates/letters_pending.html"
    context_object_name = "data"

class LetterApprove(View):
    def get(self,requset):
        id=requset.GET.get("id")
        lqs=NewsLettersModel.objects.filter(letter_id=id)
        lqs.update(status="approved")
        # id = ''
        # contact = ''
        # password = ''
        # for x in lqs:
        #     id = x.letter_id
        #     contact = x.contact_number
        # message = "we are approved your News Letter,Now people will see your Letters, letter_id:" +str(id)
        # sms.sendSms(message, contact)
        messages.success(requset, "Sucessfully Approved")
        return redirect('pendingletters')


class LetterDecline(View):
    def get(self,requset):
        id=requset.GET.get("id")
        lqs=NewsLettersModel.objects.filter(letter_id=id)
        lqs.update(status="declined")
        # id = ''
        # contact = ''
        # password = ''
        # for x in lqs:
        #     id = x.letter_id
        #     contact = x.contact_number
        # message = "we are approved your News Letter,Now people will see your Letters, letter_id:" +str(id)
        # sms.sendSms(message, contact)
        messages.success(requset, "Sucessfully declined")
        return redirect('pendingletters')

class PendingComplaints(ListView):
    queryset =ComplaintModel.objects.filter(complaint_status="pending")
    template_name ='Admin_templates/pending_complaints.html'
    context_object_name = "data"

class ApproveComplaint(View):
    def get(self,request,id):
        cqs=ComplaintModel.objects.filter(complaint_id=id)
        cqs.update(complaint_status="approved")
        messages.success(request,"Sucessfully Approved")
        return redirect('pendingcomplaints')

class DeclinedComplaint(View):
    def get(self,request,id):
        cqs=ComplaintModel.objects.filter(complaint_id=id)
        cqs.update(complaint_status="declined")
        messages.success(request,"Sucessfully declined")
        return redirect('pendingcomplaints')


class DeclineComplaintsLetters(View):
    def get(self,request):
        cqs=ComplaintModel.objects.filter(complaint_status="declined")
        nqs=NewsLettersModel.objects.filter(status="declined")
        return render(request,"Admin_templates/decline_complates_letters.html",{"data1":cqs,"data2":nqs})

class DeleteComplaint(View):
    def get(self,request,id):
        ComplaintModel.objects.get(complaint_id=id).delete()
        messages.success(request,"declined complaint deleted")
        return redirect('declined_c_l')

class DeclineLetterDelete(View):
    def get(self,request,id):
        NewsLettersModel.objects.get(letter_id=id).delete()
        messages.success(request,"declined News Letter deleted")
        return redirect('declined_c_l')

class AdminReports(View):
    def get(self,request):
        try:
            uname=request.session["uname"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired.....!"})
        else:
            return render(request,"Admin_templates/admin_home.html",{"data_reports":"To get the reports click the follwoing..!"})

class ReigisteredComplates(ListView):
    queryset = ComplaintModel.objects.filter(complaint_status="registered")
    context_object_name = "data"
    template_name ="Admin_templates/complaint_reports.html"

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

class SolvedComplaints(ListView):
    queryset = ComplaintModel.objects.filter(complaint_status="solved")
    context_object_name = "data1"
    template_name ="Admin_templates/complaint_reports.html"

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


