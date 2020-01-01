from Child_NGOs.models import NGORegistrationModel,NewsLettersModel
from Child_police.models import PoliceRegistrationModel
from Child_user.models import ComplaintModel
from rest_framework import serializers


# def checkId(id):
#     ns=NGORegistrationModel.objects.filter(ngo_id=id)
#     if ns:
#         raise serializers.ValidationError(" Sorry Id number already exist")
#     else:
#         return id
# def checkIdP(id):
#     ns=PoliceRegistrationModel.objects.filter(police_station_id=id)
#     if ns:
#         raise serializers.ValidationError(" Sorry Id number already exist")
#     else:
#         return id

class PoliceRegistrationSerializer(serializers.Serializer):
    police_station_id=serializers.CharField()
    station_place=serializers.CharField()
    station_ci_name=serializers.CharField()
    mandal=serializers.CharField()
    District=serializers.CharField()
    contact_number=serializers.CharField()
    station_mail=serializers.EmailField()
    complete_address=serializers.CharField()
    password=serializers.CharField()
    status=serializers.CharField()
    Date_of_join=serializers.DateField()

    def validate(self, attrs):
        if "@gmail.com" in attrs.get("station_mail"):
            if len(attrs.get("password"))>=2:
                return attrs
            else:
                raise serializers.ValidationError("check once mail or password")
        else:
            raise serializers.ValidationError("check once mail123 or password")

    def validate_status(self, status):
        if status=="pending":
            return status
        else:
            raise serializers.ValidationError("please ensure your status must be pending..!")

    def create(self, validated_data):
        return PoliceRegistrationModel.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.police_station_id = validated_data.get("police_station_id",instance.police_station_id )
        instance.station_place = validated_data.get("station_place",instance.station_place)
        instance.station_ci_name = validated_data.get("station_ci_name",instance.station_ci_name)
        instance.mandal =validated_data.get("mandal",instance.mandal)
        instance.District = validated_data.get("District",instance.District)
        instance.contact_number = validated_data.get("contact_number",instance.contact_number)
        instance.station_mail = validated_data.get("station_mail",instance.station_mail)
        instance.complete_address = validated_data.get("complete_address",instance.complete_address)
        instance.password = validated_data.get("password",instance.password)
        instance.status = validated_data.get("status",instance.status)
        instance.Date_of_join = validated_data.get("Date_of_join",instance.Date_of_join)
        instance.save()
        return instance

class NGORegistrationSerializer(serializers.ModelSerializer):
    ngo_id = serializers.CharField()
    class Meta:
        model=NGORegistrationModel
        fields="__all__"
    def validate_status(self, status):
        if status=="pending":
            return status
        else:
            raise serializers.ValidationError("please ensure your status must be pending..!")
class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=ComplaintModel
        fields="__all__"

