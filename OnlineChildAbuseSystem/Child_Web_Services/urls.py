"""OnlineChildAbuseSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from OnlineChildAbuseSystem import settings
from Child_Web_Services import views
from django.views.generic import TemplateView
urlpatterns = [
#police services........

path('get_police_data/',views.PoliceOperations.as_view()),
path('police_registration_request/',views.PoliceRegistrationRequest.as_view({'post':'create'})),
path('police_details_update/',views.PoliceUpdate.as_view()),

#complaint details services......
path('get_total_complaint_details/',views.GetComplaints.as_view()),

#ngo's services.........

path('get_ngo_data/',views.GetNgodetails.as_view()),
path('ngo_registration_request/',views.NgoRegistrationRequest.as_view({'post':'create'})),
path('ngo_details_update/',views.NgoUpdate.as_view()),

#regular....
path('services/',TemplateView.as_view(template_name="Main_templates/services.html"),name='services')
]
