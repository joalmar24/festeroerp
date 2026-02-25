from django.shortcuts import render, redirect
from .models import Socio
from .forms import SocioForm

def home(request):
    socios = Socio.objects.all()
    return render(request, 'socios/home.html', {'socios': socios})

def crear_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SocioForm()

    return render(request, 'socios/crear.html', {'form': form})
