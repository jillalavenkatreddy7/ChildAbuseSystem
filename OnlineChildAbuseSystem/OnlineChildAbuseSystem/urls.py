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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Child_admin/',include('Child_admin.urls')),
    path('Child_user/',include('Child_user.urls')),
    path('Child_NGOs/',include('Child_NGOs.urls')),
    path('Child_police/',include('Child_police.urls')),
    path('Child_Web_Services/',include('Child_Web_Services.urls')),
    path('',TemplateView.as_view(template_name='Main_templates/main.html')),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)