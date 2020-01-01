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

from django.urls import path,include
from django.views.generic import TemplateView
from Child_user import views
from Child_admin import download
urlpatterns = [
path('userhome/',TemplateView.as_view(template_name="User_templates/userhome.html"),name='userhome'),
path('viewnewsletters/',views.ViewNewsLetter.as_view(),name='viewnewsletters'),
path('post_complaint/',TemplateView.as_view(template_name="User_templates/post_complaint.html"),name='post_complaint'),
path('complaint_save/',views.ComplaintSave.as_view(),name='complaint_save'),
path('user_reports/',views.UserReports.as_view(),name='user_reports'),
path('uesr_registered_complaints/',views.UesrRegisteredComplaints.as_view(),name='uesr_registered_complaints'),
path('uesr_solved_complaints/',views.UserSolvedComplaints.as_view(),name='uesr_solved_complaints'),
path('download_user_solved_complaints/',download.DownloadSolvedComplaints.as_view(),name='download_user_solved_complaints'),
path('download_user_register_complaints/',download.DownloadRegisterComplaints.as_view(),name='download_user_register_complaints')
]
