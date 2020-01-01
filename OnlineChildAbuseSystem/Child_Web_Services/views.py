from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from Child_Web_Services.serilalizers import PoliceRegistrationSerializer,ComplaintSerializer,NGORegistrationSerializer
from Child_police.models import PoliceRegistrationModel
from django.core.serializers import serialize
import json
import io
from Child_NGOs.models import NGORegistrationModel,NewsLettersModel
from Child_user.models import ComplaintModel


class GetComplaints(APIView):
    def get(self,request):
        qs1=ComplaintModel.objects.filter(complaint_status="registered")
        qs2=ComplaintModel.objects.filter(complaint_status="solved")
        data=qs1.union(qs2)
        if data:
            cs=ComplaintSerializer(data,many=True)
            return Response(cs.data)
        else:
            json_data = {"message":"No complaint details available yet"}
            return Response(json_data)

class PoliceOperations(APIView):
    def get(self,request):
            pd=PoliceRegistrationModel.objects.filter(status="approved")
        # for x in pd:
        #     pdata={"police_station_id":x.police_station_id,"station_place":x.station_place,
        #       "station_ci_name":x.station_ci_name,'mandal':x.mandal,'District':x.District,
        #      "contact_number":x.contact_number,"station_mail":x.station_mail,"complete_address":x.complete_address,
        #      "status":x.status,"Date_of_join":x.Date_of_join}
        #     json_data=JSONRenderer().render(pdata)
            if pd:
                json_data = serialize("json", pd,
                                      fields=["police_station_id", "station_place", "station_ci_name", 'mandal',
                                              'District', "contact_number", "station_mail", "complete_address",
                                              "status", "Date_of_join"])
            else:
                json_data={"message":"No details available yet"}

            return Response(json_data)

class GetNgodetails(APIView):
    def get(self,request):
        nd=NGORegistrationModel.objects.filter(status="approved")
        if nd:
            json_data=serialize("json",nd,fields=["ngo_id","ngo_place","ngo_volunteer_name","mandal",
                                                  "District","contact_number","Ngo_mail","complete_address",
                                                  "status","Date_of_join"])
        else:
            json_data = {"message": "No details available yet"}
        return Response(json_data)


class PoliceRegistrationRequest(ViewSet):
    def create(self,request):
        python_dict=request.data
        prdata=PoliceRegistrationModel.objects.filter(police_station_id=python_dict['police_station_id'])
        pordata=PoliceRegistrationModel.objects.filter(contact_number=python_dict['contact_number'])

        if prdata or pordata:
            message={"msg":"Id or contact number already exist"}
            return Response(message)
        else:
            ps=PoliceRegistrationSerializer(data=python_dict)
            if ps.is_valid():
                ps.save()
                message={"msg":"detail are sended to admin and need to approve by admin"}
            else:
                message={"msg":ps.errors}
            return Response(message)


class PoliceUpdate(APIView):
    def put(self,requet):
        python_dict=requet.data
        try:
            pd=PoliceRegistrationModel.objects.get(police_station_id=python_dict['police_station_id'])
        except:
                message = {"msg":"Invalid Idno"}
                return Response(message)
        else:
            ps=PoliceRegistrationSerializer(pd,data=python_dict,partial=True)
            if ps.is_valid():
                ps.save()
                message = {"msg": "details updated"}
            else:
                message = {"msg": ps.errors}
            return Response(message)

class NgoRegistrationRequest(ViewSet):
    def create(self,request):
        python_dict=request.data
        ngdata=NGORegistrationModel.objects.filter(ngo_id=python_dict['ngo_id'])
        ngodata=NGORegistrationModel.objects.filter(contact_number=python_dict['contact_number'])
        if ngdata or ngodata:
            message = {"msg":"Idno or contact number already existed"}
            return Response(message)
        else:
            ns=NGORegistrationSerializer(data=python_dict)
            if ns.is_valid():
                ns.save()
                message={"msg":"detail are sended to admin and need to approve by admin"}
            else:
                message={"msg":ns.errors}
            return Response(message)
class NgoUpdate(APIView):
    def put(self,requet):
        python_dict=requet.data
        try:
            ns=NGORegistrationModel.objects.get(ngo_id=python_dict['ngo_id'])
        except:
                message = {"msg":"Invalid Idno"}
                return Response(message)
        else:
            ngs=NGORegistrationSerializer(ns,data=python_dict,partial=True)
            if ngs.is_valid():
                ngs.save()
                message = {"msg": "details updated"}
            else:
                message = {"msg": ngs.errors}
            return Response(message)