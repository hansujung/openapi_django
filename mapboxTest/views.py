from django.shortcuts import render

# Create your views here.

def test_map(request):
    mapboxToken = "pk.eyJ1IjoiaGFzc3p6IiwiYSI6ImNqbGdibnB0czE1dnUza3BhM3ZiZGE1MmMifQ.PdUA8uR-a7BApNBugthSQA"
    content = { "mapboxToken":mapboxToken }
    return render(request, 'mapboxTest/test_map.html', content)
