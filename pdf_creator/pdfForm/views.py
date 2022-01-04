from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    names = {
        'name': 'supi'
    }
    return render(request, 'index.html', names)
