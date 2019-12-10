from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^korea/', views.korea_map, name='korea_map'),
    url(r'^$', views.test_map, name='test_map'),
    url(r'^btn/$', views.btn_map, name='btn_map'),
    url(r'^cctvurl/$', views.cctv_url, name='cctv_url'),
    url(r'^accidurl/$', views.accid_url, name='accid_url'),
    url(r'^consturl/$', views.const_url, name='const_url'),
]