"""Weathersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from Weatherapp import views

urlpatterns = [
    url(r'^$',views.main_html,name='main_view'), #바로 맵만나오는거
    url(r'^weatherurl/$',views.weather_url,name="weather_view"), #weatherjson가져오는 url
    url(r'^airurl/$',views.air_url,name="air_view"), #air가져오는url

    url(r'^btn/$',views. btm_html,name='btn_view') #데이터까지 같이 보낸 맵

    #url(r'weather_view/$',views.weather_html,name='weather_view'),
   #path('admin/', admin.site.urls),
    #path('Weatherapp/', views.weather_html,name='my_view'),


]
