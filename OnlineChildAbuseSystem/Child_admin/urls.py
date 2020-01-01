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

from Child_admin import views




urlpatterns = [
    path('login/',TemplateView.as_view(template_name='Admin_templates/adminlogin.html'),name='adminlogin'),
    path('admincheck/',views.AdminCheck.as_view(),name='admincheck'),
    path('admin_home/',views.AdminHome.as_view(),name='admi_home'),
    path('logout/',views.Logout.as_view(),name='logout'),
    path('pendings/',views.Pendings.as_view(),name='pendings'),
    path('approving/',views.Approving.as_view(),name='approving'),
    path('approved/',views.Approved.as_view(),name='approved'),
    path('remove<int:id>/',views.Remove.as_view(),name='remove'),
    path('decline<int:id>/',views.Decline.as_view(),name='decline'),
    path('declined_req/',views.Declined_req.as_view(),name='declined_req'),
    path('pendingngo/',views.PendingNGO.as_view(),name='pendingngo'),
    path('ngoapprove/',views.NGOApprove.as_view(),name='ngoapprove'),
    path('approvedngo/',views.ApprovedNGO.as_view(),name='approvedngo'),
    path('ngodecline/',views.DeclineNgo.as_view(),name='ngodecline'),
    path('ngoremove/',views.NGORemove.as_view(),name='ngoremove'),
    path('declinengo/',views.DeclineNGORequests.as_view(),name='declinengo'),
    path('pendingletters/',views.PendinglettersData.as_view(),name='pendingletters'),
    path('letter_approve/',views.LetterApprove.as_view(),name='letter_approve'),
    path('letter_decline/',views.LetterDecline.as_view(),name='letter_decline'),
    path('pendingcomplaints/',views.PendingComplaints.as_view(),name='pendingcomplaints'),
    path('approve_complaint<int:id>/',views.ApproveComplaint.as_view(),name='approve_complaint'),
    path('decline_complaint<int:id>/',views.DeclinedComplaint.as_view(),name='decline_complaint'),
    path('declined_complaints_letters/',views.DeclineComplaintsLetters.as_view(),name='declined_c_l'),
    path('delete_complaint<int:id>/',views.DeleteComplaint.as_view(),name='delete_complaint'),
    path('decline_letter_delete<int:id>/',views.DeclineLetterDelete.as_view(),name='decline_letter_delete'),
    path('admin_reports/',views.AdminReports.as_view(),name='admin_reports'),
    path('registered_complaints/',views.ReigisteredComplates.as_view(),name='registered_complaints'),
    path('download_register_complaints/',views.DownloadRegisterComplaints.as_view(),name='download_register_complaints'),
    path('solved_complaints/',views.SolvedComplaints.as_view(),name='solved_complaints'),
    path('download_solved_complaints/',views.DownloadSolvedComplaints.as_view(),name='download_solved_complaints')
]
