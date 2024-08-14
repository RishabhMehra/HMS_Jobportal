"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse
from HMS import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.training),
    path("trainadmin/", views.trainadmin),
    path("adminhome/", views.adminhome),


    path("trainuser/", views.trainuser),
    path("usersignup/", views.usersignup),
    path("userhome/", views.userhome),
    path("viewusers/", views.viewusers),
    path("delete_user/<int:pid>/", views.delete_user),


    path("trainrecruiter/", views.trainrecruiter),
    path("recsignup/", views.recsignup),
    path("rechome/", views.rechome),
    path("delete_recruiter/<int:pid>/", views.delete_recruiter),
    path("pending/", views.pending),
    path("accepted/", views.accepted),
    path("rejected/", views.rejected),
    path("allrecruiters/", views.allrecruiters),


  
    path("Logout/", views.Logout),
    path("changestatus/<int:pid>/", views.changestatus),


   
    path("passadmin/", views.passadmin),
    path("passuser/", views.passuser),
    path("passrec/", views.passrec),



    path("addjobrec/", views.addjobrec),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
