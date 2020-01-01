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
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

from Child_police import views
from Child_admin import download

urlpatterns = [
    path('RegistrationLogin/',TemplateView.as_view(template_name='Police_templates/p_register_login.html'),name='polregislogin'),
    path('p_register/',TemplateView.as_view(template_name='Police_templates/police_register.html'),name='p_register'),
    path('register_pending/',views.RegisterPending.as_view(),name='register_pending'),
    path('police_validate/',views.PoliceValidate.as_view(),name='police_validate'),
    path('police_home',TemplateView.as_view(template_name="Police_templates/police_home.html"),name='police_home'),
    path('viewpprofile/',views.ViewPprofile.as_view(),name='viewpprofile'),
    path('police_update/',views.UpdatePolice.as_view(),name='police_update'),
    path('station_update/',views.StationUpdateSave.as_view(),name='station_update'),
    path('p_changepassword/',views.ChangePolicePassword.as_view(),name='p_changepassword'),
    path('p_change_save/',views.ChangeSave.as_view(),name='p_change_save'),
    path('p_logout/',views.PoliceLogout.as_view(),name='p_logout'),
    path('viewcomplaints/',views.ViewComplaints.as_view(),name='viewcomplaints'),
    path('register_complaint<int:id>/',views.RegiterComplaint.as_view(),name='register_complaint'),
    path('solved_complaint<int:id>/',views.SolvedComplaints.as_view(),name='solved_complaint'),
    path('police_reports/',views.PoliceReports.as_view(),name='police_reports'),
    path('police_solved_reports/',views.PoliceSolvedReports.as_view(),name='police_solved_reports'),
    path('police_download_solved_complaints/',download.DownloadSolvedComplaints.as_view(),name='police_download_solved_complaints'),
    path('police_registered_reports/',views.PoliceRegisteredReports.as_view(),name='police_registered_reports'),
    path('police_download_register_complaints',download.DownloadRegisterComplaints.as_view(),name='police_download_register_complaints')
]
