from django.shortcuts import render


# Create your views here.
def google_map(request):
    return render(request, 'streetmap/google_map.html', {})
