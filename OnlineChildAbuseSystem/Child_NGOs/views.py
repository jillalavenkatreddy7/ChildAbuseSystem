from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from Child_NGOs.models import NGORegistrationModel,NewsLettersModel
from django.contrib import messages
class NGOPendingRegister(View):
    def post(self,requset):
        id=requset.POST.get("nid")
        place =requset.POST.get("np")
        mandal =requset.POST.get("nm")
        distict =requset.POST.get("nd")
        volunteer =requset.POST.get("nvn")
        number =requset.POST.get("ncn")
        mail =requset.POST.get("nml")
        address =requset.POST.get("nca")
        pword =requset.POST.get("pword")
        status="pending"
        try:
            NGORegistrationModel.objects.get(ngo_id=id)
        except NGORegistrationModel.DoesNotExist:
            NGORegistrationModel(ngo_id=id,ngo_place=place,mandal=mandal,District=distict,
                                 ngo_volunteer_name=volunteer,contact_number=number,
                                 Ngo_mail=mail,complete_address=address,password=pword,status=status).save()
            messages.success(requset, "your details need to approve by admin.please wait untill approved..! ")
            return redirect('ngoregister')
        else:
            messages.success(requset, "Idno already Existed")
            return redirect('ngoregister')

class NGOLoginCheck(View):
    def post(self,requset):
        id=requset.POST.get("id")
        pword=requset.POST.get("pword")
        try:
            ndata=NGORegistrationModel.objects.get(ngo_id=id)
        except NGORegistrationModel.DoesNotExist:
            messages.success(requset, "Invalid Idno")
            return redirect('ngoregislogin')
        else:
            if ndata.status=="approved":
                try:
                    NGORegistrationModel.objects.get(ngo_id=id,password=pword)
                    requset.session["nid"]=id
                except NGORegistrationModel.DoesNotExist:
                    messages.success(requset, "Invalid ID or Password")
                    return redirect('ngoregislogin')
                else:
                    return redirect('ngohome')
            else:
                messages.success(requset,"Sorry your Invalid User")
                return redirect('ngoregislogin')

class NGOLogout(View):
    def get(self,request):
        try:
            del request.session["nid"]
        except:
            return render(request,"Main_templates/main.html",{"data":"Sucessfully logged out"})
        else:
            return render(request, "Main_templates/main.html", {"data": "Sucessfully logged out"})

class ViewNgoprofile(View):
    def get(self,requset):
        try:
            id=requset.session["nid"]
        except:
            return render(requset, "Main_templates/main.html", {"data":"Sorry your Session expired.....!"})
        else:
            ndata=NGORegistrationModel.objects.filter(ngo_id=id)
            return render(requset,"NGOS_templates/ngo_home.html",{"data":ndata})

class NgoUpdate(DetailView):
    model = NGORegistrationModel
    template_name = "NGOS_templates/ngo_home.html"
    context_object_name = "x"


class NgoUpdateSave(View):
    def post(self,requset):
        id = requset.POST.get("nid")
        place = requset.POST.get("np")
        mandal = requset.POST.get("nm")
        distict = requset.POST.get("nd")
        volunteer = requset.POST.get("nvn")
        number = requset.POST.get("ncn")
        mail = requset.POST.get("nml")
        address = requset.POST.get("nca")
        ndata=NGORegistrationModel.objects.filter(ngo_id=id)
        ndata.update(ngo_place=place,mandal=mandal,District=distict,
                                 ngo_volunteer_name=volunteer,contact_number=number,
                                 Ngo_mail=mail,complete_address=address)
        messages.success(requset,"updated sucessfully")
        return redirect('ngohome')

class NgoChangePasword(View):
    def get(self,request):
        try:
            id=request.session["nid"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired......!"})
        else:
            np=NGORegistrationModel.objects.get(ngo_id=id)
            return render(request,"NGOS_templates/ngo_home.html",{"np":np})

class Changepassword(View):
    def post(self,request):
        pword=request.POST.get("pword")
        try:
            id=request.session["nid"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired....!"})
        else:
            np=NGORegistrationModel.objects.filter(ngo_id=id)
            np.update(password=pword)
            messages.success(request, "Changed sucessfully")
            return redirect('ngohome')

class PostLetter(View):
    def get(self,request):
        try:
            id=request.session["nid"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired....!"})
        else:
            ndata=NGORegistrationModel.objects.get(ngo_id=id)
            return render(request,"NGOS_templates/ngo_home.html",{"newsdata":ndata})

class PostNews(View):
    def post(self,request):
        try:
            id=request.session["nid"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired....!"})
        else:
            id=request.POST.get("id")
            file=request.FILES["file"]
            status="pending"
            nd=NGORegistrationModel.objects.get(ngo_id=id)
            NewsLettersModel(letter_file=file,status=status,address=nd.complete_address,sender_name=nd.ngo_volunteer_name,
                             contact_number=nd.contact_number,sender_mail=nd.Ngo_mail,place=nd.mandal).save()
            messages.success(request, "Posted sucessfully")
            return redirect('ngohome')

class ViewNewsLetters(View):
    def get(self,request):
        try:
            id=request.session["nid"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired......!"})
        else:
            pending_data=NewsLettersModel.objects.filter(status="pending")
            approved_data=NewsLettersModel.objects.filter(status="approved")
            declined_data=NewsLettersModel.objects.filter(status="declined")
            return render(request,"NGOS_templates/ngo_home.html",{"pending_data":pending_data,"approved_data":approved_data,"declined_data":declined_data})

class NewsDelete(View):
    def get(self,request):
        try:
            id=request.session["nid"]
        except:
            return render(request, "Main_templates/main.html", {"data": "Sorry your Session expired.....!"})
        else:
            id=request.GET.get("id")
            NewsLettersModel.objects.get(letter_id=id).delete()
            messages.success(request, "Deleted sucessfully")
            return redirect('ngohome')

