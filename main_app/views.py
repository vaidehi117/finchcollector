from django.shortcuts import render
from .models import Finch

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def finchs_index(request):
    return render(request, 'finchs/index.html', {
        'finchs': finchs
    })