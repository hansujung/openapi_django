from django.shortcuts import render

# Create your views here.

def test_map(request):
    mapboxToken = Token
    content = { "mapboxToken":mapboxToken }
    return render(request, 'mapboxTest/test_map.html', content)
