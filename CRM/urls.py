"""
URL configuration for CRM project.

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

from crm_home import views
from lead.views import LeadViewSet
from task.views import TaskList
from django.contrib import admin
from django.urls import path, include
from customer.views import CustomerList
from appointment.views import AppointmentList
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from account.views import UserRequestList,UserList,CompanyRequestList


router = DefaultRouter()
router.register(r'appointment',AppointmentList)
#Account
router.register(r'user_request',UserRequestList)
router.register(r'user_list',UserList)
router.register(r'company_request',CompanyRequestList)
#
router.register(r'customer',CustomerList)
router.register(r'lead',LeadViewSet)
router.register(r'task',TaskList)


urlpatterns = [
    
    ################### API PART ########################################
    path('api/',include(router.urls)),

    #################### CRM_HOME URLS ########################################
    path('',views.home, name="home"),
    path('dash/', views.dashboard, name="dashboard"),
    path('profile/',views.my_profile, name="profile_page"),
    path('update-profile/', views.update_user_profile, name='update_profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='crm_home/change_password.html', success_url='/profile/' ), name='change_password'),
    # path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
   
    ################### ACCOUNT URL'S #########################################
    path('', include('account.urls')),
    #  path('admin/', admin.site.urls),
    
    ################### ADMIN URL'S ###########################################
    path('admin/', admin.site.urls),
    
    ################### APPOINTMENT URL'S #####################################
    path('appointment/', include('appointment.urls')),
    
    ################### LEAD URL'S ############################################
    path('lead/', include('lead.urls')),
    
    ################### TASK URL'S ############################################
    path('task/', include('task.urls')),
    
    ################### CUSTOMER URL'S ########################################
    path('customer/', include('customer.urls')),

    ################### Search ########################################
    path('search/', views.master_search, name='master_search'),

    ########################### THE END #######################################
]
