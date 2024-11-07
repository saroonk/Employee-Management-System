"""
URL configuration for Employee_mangement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from employeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminhome/',views.adminhome,name='Adminhome'),
    path('userregistration/',views.user_reg,name='user_reg'),
    path('userhome',views.userhome,name='userhome'),
    path('userprofile',views.userprofile,name='userprofile'),
    path('userupdate/',views.userupdate,name='userupdate'),
    path('',views.logins,name='logins'),
    path('logout/',views.logout,name='logout'),
    path('viewemployee/',views.view_employee,name='view_employee'),
    path("approveemployee/<int:aid>",views.approverequest,name="approverequest"),
    path("disaproveemployee/<int:aid>",views.disaproverequest,name="disaproveemployee"),
    path("deleteemployee/<int:did>",views.deleterequest,name="confirmrequest"),

   

    







]
