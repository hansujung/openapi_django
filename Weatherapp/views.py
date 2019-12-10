from django.shortcuts import render
from django.shortcuts import render_to_response
from urllib.request import urlopen
import json

from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET

"""
weatherurl = 'http://api.openweathermap.org/data/2.5/box/city?bbox=126.7,36.9,127.8,38.5,11&cluster=yes&format=json&APPID=45177ff490cc791de1def08e071936b1'
wdata = urlopen(weatherurl).read()
jwdata = json.loads(wdata)
kwdata = jwdata['list']
js_data = json.dumps(kwdata)

airurl='https://api.waqi.info/map/bounds/?latlng=39.379436,116.091230,40.235643,116.784382&token=2089b05319f581b79a51540823d2984060a0127e'
adata=urlopen(airurl).read()
jadata=json.loads(adata)
kadata=jadata['data']
#print(kadata)
"""


class Data:

    def getWeather(self):
        weatherurl = 'http://api.openweathermap.org/data/2.5/box/city?bbox=126.7,36.9,127.8,38.5,11&cluster=yes&format=json&APPID=45177ff490cc791de1def08e071936b1'
        wdata = urlopen(weatherurl).read()
        jwdata = json.loads(wdata)
        kwdata = jwdata['list']
        kwdata = json.dumps(kwdata, ensure_ascii=False)

        # weather_arr=[]
        # weather_arr.append(json.dumps(kwdata, ensure_ascii=False))
        # return weather_arr

        return kwdata

    def getAir(self):
        airurl = 'https://api.waqi.info/map/bounds/?latlng=37.345131,126.709022,37.601629,127.185752&token=41da8ebfbc9cc68442af347291689e8cbeb5a9b1' #다시바운드 찾기
        adata = urlopen(airurl).read()
        jadata = json.loads(adata)
        kadata = jadata['data']
        kadata = json.dumps(kadata, ensure_ascii=False)

        # air_arr=[]
        # air_arr.append(json.dumps(kadata, ensure_ascii=False))
        # return air_arr

        return kadata


@require_GET
def weather_url(request):
    data = Data();
    return HttpResponse(data.getWeather(), content_type="application/json; charset=utf-8")
    # return HttpResponse(json.dumps(data.getWeather(), ensure_ascii=False), content_type="application/json; charset=utf-8")


@require_GET
def air_url(request):
    data = Data();
    return HttpResponse(data.getAir(), content_type="application/json; charset=utf-8")
    # return HttpResponse(json.dumps(data.getAir(), ensure_ascii=False), content_type="application/json; charset=utf-8")


def main_html(request):
    return render(request, 'Weatherapp/Mainmap.html')


# Create your views here.
def btm_html(request):
    data = Data();
    content = {'weather_list': data.getWeather(), 'air_list': data.getAir()}
    return render(request, 'Weatherapp/Mainmap.html', content)
