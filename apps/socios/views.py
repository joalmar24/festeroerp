from django.shortcuts import render
from .models import Socio

def home(request):
    socios = Socio.objects.filter(estado=True)
    return render(request, 'socios/home.html', {'socios': socios})
