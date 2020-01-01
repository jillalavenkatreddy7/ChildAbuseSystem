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
from Child_NGOs import views
urlpatterns = [
path('ngoregislogin/',TemplateView.as_view(template_name="NGOS_templates/ngo_login.html"),name='ngoregislogin'),
path('ngoregister/',TemplateView.as_view(template_name="NGOS_templates/ngo_register.html"),name='ngoregister'),
path('ngopendingregister/',views.NGOPendingRegister.as_view(),name='ngopendingregister'),
path('ngocheck/',views.NGOLoginCheck.as_view(),name='ngocheck'),
path('NGOHome/',TemplateView.as_view(template_name="NGOS_templates/ngo_home.html"),name='ngohome'),
path('ngologout/',views.NGOLogout.as_view(),name='ngologout'),
path('viewNgoprofile/',views.ViewNgoprofile.as_view(),name='viewNgoprofile'),
path('ngoupdate<int:pk>/',views.NgoUpdate.as_view(),name='ngoupdate'),
path('ngoupdatesave/',views.NgoUpdateSave.as_view(),name='ngoupdatesave'),
path('nchange_password/',views.NgoChangePasword.as_view(),name='nchange_password'),
path('Change/',views.Changepassword.as_view(),name='Change'),
path('postletter/',views.PostLetter.as_view(),name='postletter'),
path('postnews/',views.PostNews.as_view(),name='postnews'),
path('viewletters/',views.ViewNewsLetters.as_view(),name='viewletters'),
path('newsdelete/',views.NewsDelete.as_view(),name='newsdelete')
]
