"""projektSzpital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from pacjenci.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('list/', patient_list, name='patient_list'),
    path('patient/<patient_id>/', patient_info, name='patient_info'),
    path('studies/<studies_id>/', studies_info, name='studies_info'),
    path('series/<series_id>/', series_info, name='series_info'),
]