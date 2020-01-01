from django.shortcuts import render,redirect
from django.views.generic import View,ListView
from Child_NGOs.models import NewsLettersModel
from django.contrib import messages
from Child_user.models import ComplaintModel

class ViewNewsLetter(ListView):
    queryset = NewsLettersModel.objects.filter(status="approved")
    model = NewsLettersModel
    template_name = 'User_templates/view_letters.html'
    context_object_name = "data"

class ComplaintSave(View):
    def post(self,request):
        ctype=request.POST.get("type")
        if ctype=="Child Abusing":
            sender_name=request.POST.get("csname")
            place=request.POST.get("place")
            number=request.POST.get("pnumber")
            complaint_place=request.POST.get("cplace")
            complaint_details=request.POST.get("cd")
            status="pending"
            ComplaintModel(complaint_sender_name=sender_name,complaint_sender_place=place,complaint_sender_number=number,
                           complaint_details=complaint_details,complainting_place=complaint_place,complaint_status=status).save()
            messages.success(request,"Thank You for complaint..your complaint sended sucessfully..!")
            return redirect('post_complaint')
        else:
            messages.success(request,"Sorry unable to process your request,Complaints Should be on childs only..!")
            return redirect('post_complaint')

class UserReports(View):
    def get(self,request):
        return render(request,"User_templates/userhome.html",{"data_reports":"To get the reports click the follwoing..!"})

class UesrRegisteredComplaints(ListView):
    queryset = ComplaintModel.objects.filter(complaint_status="registered")
    context_object_name = "data"
    template_name ="User_templates/user_complaint_reports.html"

class UserSolvedComplaints(ListView):
    queryset = ComplaintModel.objects.filter(complaint_status="solved")
    context_object_name = "data1"
    template_name ="User_templates/user_complaint_reports.html"