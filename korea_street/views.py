from django.shortcuts import render
import datetime
import urllib.request
import urllib.response
import urllib
import xml.etree.ElementTree as eltree
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET


# traffic information (CCTV, Event(Accident, Construction)
class GetData:
    API_KEY = '1534915956107'

    # params = "key=%s&ReqType=2&MinX=124.100000&MaxX=129.800000&MinY=33.100000&MaxY=39.100000&type=" % API_KEY # 전체
    params = "key=%s&ReqType=2&MinX=126.100000&MaxX=127.800000&MinY=36.900000&MaxY=38.500000&type=" % API_KEY # 경기도 부분만

    cctv_url = 'http://openapi.its.go.kr:8081/api/NCCTVInfo?'
    const_url = 'http://openapi.its.go.kr:8082/api/NEventIdentity?'
    accid_url = 'http://openapi.its.go.kr:8082/api/NIncidentIdentity?'

    # CCTV URL Return
    def getRTCCTV(self, lng, lat):
        param_cctv = "key=%s&ReqType=2&MinX=%s&MaxX=%s&MinY=%s&MaxY=%s&type=" % (self.API_KEY, str(lng-0.000001), str(lng+0.000001), str(lat-0.000001), str(lat+0.000001))
        cctv_ex_data = urllib.request.urlopen(self.cctv_url + param_cctv + "ex")
        cctv_ex_xml = cctv_ex_data.read().decode('utf-8')
        cctv_ex_tree = eltree.fromstringlist(cctv_ex_xml)

        cctv_its_data = urllib.request.urlopen(self.cctv_url + param_cctv + "its")
        cctv_its_xml = cctv_its_data.read().decode('utf-8')
        cctv_its_tree = eltree.fromstringlist(cctv_its_xml)

        cctv_ex_arr = []
        cctv_its_arr = []
        cctv_arr = []

        for i in cctv_ex_tree.findall('data'):
            data = {"content": i.find('cctvurl').text}
            cctv_ex_arr.append(json.dumps(data, ensure_ascii=False))

        for i in cctv_its_tree.findall('data'):
            data = {"content": i.find('cctvurl').text}
            cctv_its_arr.append(json.dumps(data, ensure_ascii=False))

        cctv_arr.extend(cctv_ex_arr)
        cctv_arr.extend(cctv_its_arr)

        print(cctv_arr)
        return cctv_arr

    # CCTV DATA Return
    def getCCTV(self):

        cctv_ex_data = urllib.request.urlopen(self.cctv_url + self.params + "ex")
        cctv_ex_xml = cctv_ex_data.read().decode('utf-8')
        cctv_ex_tree = eltree.fromstringlist(cctv_ex_xml)

        cctv_its_data = urllib.request.urlopen(self.cctv_url + self.params + "its")
        cctv_its_xml = cctv_its_data.read().decode('utf-8')
        cctv_its_tree = eltree.fromstringlist(cctv_its_xml)

        cctv_ex_arr = []
        cctv_its_arr = []
        cctv_arr = []

        for i in cctv_ex_tree.findall('data'):
            data = {"title": i.find('cctvname').text,
                    "lat": float(i.find('coordy').text),
                    "lng": float(i.find('coordx').text),
                    "content": i.find('cctvurl').text
                    }
            cctv_ex_arr.append(json.dumps(data, ensure_ascii=False))

        for i in cctv_its_tree.findall('data'):
            data = {"title": i.find('cctvname').text,
                    "lat": float(i.find('coordy').text),
                    "lng": float(i.find('coordx').text),
                    "content": i.find('cctvurl').text
                    }
            cctv_its_arr.append(json.dumps(data, ensure_ascii=False))

        cctv_arr.extend(cctv_ex_arr)
        cctv_arr.extend(cctv_its_arr)

        return cctv_arr

    # Accident DATA Return
    def getAcci(self):

        accid_ex_data = urllib.request.urlopen(self.accid_url + self.params + "ex")
        accid_ex_xml = accid_ex_data.read().decode('utf-8')
        accid_ex_tree = eltree.fromstringlist(accid_ex_xml)

        accid_its_data = urllib.request.urlopen(self.accid_url + self.params + "its")
        accid_its_xml = accid_its_data.read().decode('utf-8')
        accid_its_tree = eltree.fromstringlist(accid_its_xml)

        accid_ex_arr = []
        accid_its_arr = []
        accid_arr = []

        for i in accid_ex_tree.findall('data'):
            data = {"title": i.find('incidentmsg').text,
                    "lat": float(i.find('coordy').text),
                    "lng": float(i.find('coordx').text),
                    "content": i.find('incidentmsg').text
                    }
            accid_ex_arr.append(json.dumps(data, ensure_ascii=False))

        for i in accid_its_tree.findall('data'):
            data = {"title": i.find('incidentmsg').text,
                    "lat": float(i.find('coordy').text),
                    "lng": float(i.find('coordx').text),
                    "content": i.find('incidentmsg').text
                    }
            accid_its_arr.append(json.dumps(data, ensure_ascii=False))

        accid_arr.extend(accid_ex_arr)
        accid_arr.extend(accid_its_arr)

        return accid_arr

    # Construction DATA Return
    def getConst(self):

        const_ex_data = urllib.request.urlopen(self.const_url + self.params + "ex")
        const_ex_xml = const_ex_data.read().decode('utf-8')
        const_ex_tree = eltree.fromstringlist(const_ex_xml)

        const_its_data = urllib.request.urlopen(self.const_url + self.params + "its")
        const_its_xml = const_its_data.read().decode('utf-8')
        const_its_tree = eltree.fromstringlist(const_its_xml)

        const_ex_arr = []
        const_its_arr = []
        const_arr = []

        for i in const_ex_tree.findall('data'):
            data = {"title": i.find('eventstatusmsg').text,
                    "lat": float(i.find('coordy').text),
                    "lng": float(i.find('coordx').text),
                    "content": i.find('eventstatusmsg').text
                    }
            const_ex_arr.append(json.dumps(data, ensure_ascii=False))

        for i in const_its_tree.findall('data'):
            data = {"title": i.find('eventstatusmsg').text,
                    "lat": float(i.find('coordy').text),
                    "lng": float(i.find('coordx').text),
                    "content": i.find('eventstatusmsg').text
                    }
            const_its_arr.append(json.dumps(data, ensure_ascii=False))

        const_arr.extend(const_ex_arr)
        const_arr.extend(const_its_arr)

        return const_arr


# Create your views here.
def korea_map(request):
    return render(request, 'korea_map/korea_map.html', {})

def test_map(request):
    # mapboxToken = "pk.eyJ1IjoiYWljdCIsImEiOiJjamxmeHZnMnAwaWlrM3ZwMTFwZzNzcDZrIn0.VlZtCnZpAgFtjgy8g1zRyA"
    mapboxToken = "pk.eyJ1IjoiaGFzc3p6IiwiYSI6ImNqbGdibnB0czE1dnUza3BhM3ZiZGE1MmMifQ.PdUA8uR-a7BApNBugthSQA"
    # getDate = GetData()
    # content = {'cctv_list': getDate.getCCTV(), "accid_list": getDate.getAcci(), "const_list" : getDate.getConst(), "mapboxToken":mapboxToken}
    content = { "mapboxToken":mapboxToken }
    return render(request, 'korea_map/test_map.html', content)

def btn_map(request):
    getDate = GetData()
    content = {'cctv_list': getDate.getCCTV(), "accid_list": getDate.getAcci(), "const_list" : getDate.getConst()}
    return render(request, 'korea_map/btn_map.html', content)


# only data return
@require_GET
def cctv_url(request):
    getDate = GetData()
    # getDate.getRTCCTV(127.09706, 37.40665)
    print(datetime.datetime.now(), "CCTV")
    return HttpResponse(json.dumps(getDate.getCCTV(), ensure_ascii=False), content_type="application/json; charset=utf-8")

@require_GET
def accid_url(request):
    getDate = GetData()
    print(datetime.datetime.now(), "Accident")
    return HttpResponse(json.dumps(getDate.getAcci(), ensure_ascii=False), content_type="application/json; charset=utf-8")

@require_GET
def const_url(request):
    getDate = GetData()
    print(datetime.datetime.now(), "Construction")
    return HttpResponse(json.dumps(getDate.getConst(), ensure_ascii=False), content_type="application/json; charset=utf-8")





# # information (public data portal)
# class GetOtherData:
#     DATA_SET_API_KEY = "afYQPSYR8BIhn6sZe4InwLX8vBfZfXYbKkVBHU9CAIXmTbqvc4fcn6sinGJTQ9529dAwEW2XgTDC5fz7pKEzAg%3D%3D"
#     elcty_chrstn_url = 'http://api.data.go.kr/openapi/'
#
#     def getElctyCarChrstn(self):
#         param_elcty = 'elcty-car-chrstn-std?serviceKey=%s&s_page=1&s_list=10000&type=json' % self.DATA_SET_API_KEY
#         elcty_data = urllib.request.urlopen(self.elcty_chrstn_url + param_elcty)
#         elcty_json = json.load(elcty_data)
#         print(len(elcty_json), elcty_json[1])
#         return elcty_json
#
# @require_GET
# def elcty_url(request):
#     getOtherData = GetOtherData()
#     print(datetime.datetime.now(), "ElctyCarChrstn")
#     return HttpResponse(json.dumps(getOtherData.getElctyCarChrstn(), ensure_ascii=False), content_type="application/json; charset=utf-8")


