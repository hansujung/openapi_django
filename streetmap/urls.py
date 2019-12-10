from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.google_map, name='google_map'),
]