"""
URL configuration for ethnoeswalletapp project.

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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from myapp.views import get_balance, get_financial_data, get_savings_plans, recent_activities_data

urlpatterns = [
    path('recent_activities_data/', recent_activities_data, name='recent-activities-data'),
    path('get_balance/', get_balance, name='get-balance'),
    path('savings-plans/', get_savings_plans, name='savings-plans'),
    path('financial-data/', get_financial_data, name='financial_data'),
]
