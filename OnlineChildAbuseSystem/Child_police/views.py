from django.shortcuts import render,redirect
from django.views.generic import View
from Child_police.models import PoliceRegistrationModel
from django.contrib import messages
from django.views.generic import DetailView,ListView
from Child_user.models import ComplaintModel
class RegisterPending(View):
    def post(self,requset):
        station_id=requset.POST.get("sid")
        station_place =requset.POST.get("sp")
        station_mandal =requset.POST.get("sm")
        station_distict =requset.POST.get("sd")
        station_ci_si =requset.POST.get("scs")
        station_number =requset.POST.get("scn")
        station_mail =requset.POST.get("sm")
        station_adress =requset.POST.get("sca")
        station_pword =requset.POST.get("pword")
        status="pending"
        try:
            PoliceRegistrationModel.objects.get(police_station_id=station_id)
        except PoliceRegistrationModel.DoesNotExist:
            PoliceRegistrationModel(police_station_id=station_id,station_place=station_place,
                                mandal=station_mandal,District=station_distict,
                                station_ci_name=station_ci_si,contact_number=station_number,
                                station_mail=station_mail,complete_address=station_adress,password=station_pword,status=status).save()
            messages.success(requset, "your details need to approve by admin.please wait untill approved..! ")
            return redirect('p_register')
        else:
            messages.success(requset, "Inavalid IDNO ")
            return redirect('p_register')

class PoliceValidate(View):
    def post(self,req):
        id=req.POST.get("id")
        pword=req.POST.get("pword")
        try:
            pobject=PoliceRegistrationModel.objects.get(police_station_id=id)
        except PoliceRegistrationModel.DoesNotExist:
            messages.success(req,"Invalid idno")
            return redirect('polregislogin')
        else:
            state=pobject.status
            if state=="approved":
                try:
                    PoliceRegistrationModel.objects.get(police_station_id=id,password=pword)
                    req.session["police_id"] = id
                except:
                    messages.success(req, "Invalid idno or password")
                    return redirect('polregislogin')
                else:
                    return redirect('police_home')
            else:
                messages.success(req, "Iam sorry..!Your invalid user..")
                return redirect('polregislogin')

class ViewPprofile(View):
    def get(self,request):
        try:
            id=request.session["police_id"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired.....!"})
        else:
            pdata=PoliceRegistrationModel.objects.filter(police_station_id=id)
            return render(request,'Police_templates/police_home.html',{"data":pdata})

class UpdatePolice(View):
    def get(self,request):
        id=request.GET.get("id")
        pdata=PoliceRegistrationModel.objects.get(police_station_id=id)
        return render(request,'Police_templates/police_home.html',{"data1":pdata})

class StationUpdateSave(View):
    def post(self,requset):
        station_id = requset.POST.get("sid")
        station_place = requset.POST.get("sp")
        station_mandal = requset.POST.get("sm")
        station_distict = requset.POST.get("sd")
        station_ci_si = requset.POST.get("scs")
        station_number = requset.POST.get("scn")
        station_mail = requset.POST.get("sm")
        station_address = requset.POST.get("sca")
        psdata=PoliceRegistrationModel.objects.filter(police_station_id=station_id)
        psdata.update(station_place=station_place,
                                mandal=station_mandal,District=station_distict,
                                station_ci_name=station_ci_si,contact_number=station_number,
                                station_mail=station_mail,complete_address=station_address)
        messages.success(requset,"Sucessfully Updated")
        return redirect('police_home')

class ChangePolicePassword(View):
    def get(self,req):
        try:
            id=req.session["police_id"]
        except:
            return render(req, "Main_templates/main.html", {"data": "Sorry your Session expired.....!"})
        else:
            data3=PoliceRegistrationModel.objects.get(police_station_id=id)
            return render(req, 'Police_templates/police_home.html', {"data23":data3})

class ChangeSave(View):
    def post(self,req):
        p=req.POST.get("changed")
        id = req.session["police_id"]
        data3 = PoliceRegistrationModel.objects.filter(police_station_id=id)
        data3.update(password=p)
        messages.success(req,"Sucessfully Changed")
        return redirect('police_home')

class PoliceLogout(View):
    def get(self,req):
        try:
            del req.session["police_id"]
        except:
            return render(req,"Main_templates/main.html",{"data":"Sucesss fully logged out"})
        else:
            return render(req, "Main_templates/main.html", {"data": "Sucesss fully logged out"})

class ViewComplaints(View):
    def get(self,req):
        try:
            id=req.session["police_id"]
        except:
            return render(req, "Main_templates/main.html", {"data": "Sorry your Session expired.....!"})
        else:
            data3=ComplaintModel.objects.filter(complaint_status="approved")
            data4=ComplaintModel.objects.filter(complaint_status="registered")
            data5=ComplaintModel.objects.filter(complaint_status="solved")
            return render(req, 'Police_templates/complaints.html', {"data":data3,"data1":data4,"data2":data5})
class RegiterComplaint(View):
    def get(self,request,id):
        cqs=ComplaintModel.objects.filter(complaint_id=id)
        cqs.update(complaint_status="registered")
        messages.success(request,"complaint registered")
        return redirect('viewcomplaints')

class SolvedComplaints(View):
    def get(self,request,id):
        cqs=ComplaintModel.objects.filter(complaint_id=id)
        cqs.update(complaint_status="solved")
        messages.success(request,"complaint Solved")
        return redirect('viewcomplaints')

class PoliceReports(View):
    def get(self,request):
        try:
            id=request.session["police_id"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired.....!"})
        else:
            return render(request,"Police_templates/police_home.html",{"data_reports":"To get the reports click the follwoing..!"})

class PoliceSolvedReports(ListView):
    queryset = ComplaintModel.objects.filter(complaint_status="solved")
    context_object_name = "data1"
    template_name ="Police_templates/police_complaint_reports.html"

class PoliceRegisteredReports(ListView):
    queryset = ComplaintModel.objects.filter(complaint_status="registered")
    context_object_name = "data"
    template_name ="Police_templates/police_complaint_reports.html"