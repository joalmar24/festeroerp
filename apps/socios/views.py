from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Socio
from .forms import SocioForm
from django.http import JsonResponse
from .models import Condicion

def home(request):
    socios = Socio.objects.filter(estado=True)
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
def editar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)

    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SocioForm(instance=socio)

    return render(request, 'socios/crear.html', {'form': form})
def baja_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    socio.estado = False
    socio.save()
    return redirect('home')

def cargar_condiciones(request):
    tipo_id = request.GET.get('tipo_id')
    condiciones = Condicion.objects.filter(tipo_id=tipo_id).values('id', 'nombre')
    return JsonResponse(list(condiciones), safe=False)