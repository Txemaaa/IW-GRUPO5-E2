
from django.shortcuts import render, redirect, get_object_or_404
from .models import Turno, Empleado, Parte_Trabajo
from .forms import TurnoForm, EmpleadoForm, ParteTrabajoForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def inicio(request):
    return render(request, 'Gestion/index.html')

# VISTAS TURNOS

def lista_turnos(request):
    turnos = Turno.objects.all().order_by('fecha')
    return render(request, 'Gestion/lista_turnos.html', {'turnos': turnos})

def crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_turnos')
    else:
        form = TurnoForm()
    return render(request, 'Gestion/crear_turno.html', {'form': form})

def editar_turno(request, pk):
    turno = get_object_or_404(Turno, pk=pk)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('lista_turnos')
    else:
        form = TurnoForm(instance=turno)
    return render(request, 'Gestion/editar_turno.html', {'form': form, 'turno': turno})

def borrar_turno(request, pk):
    turno = get_object_or_404(Turno, pk=pk)
    if request.method == 'POST':
        turno.delete()
        return redirect('lista_turnos')
    return render(request, 'Gestion/borrar_turno.html', {'turno': turno})


# VISTAS EMPLEADOS

def lista_empleados(request):
    empleados = Empleado.objects.all().order_by('apellido')
    return render(request, 'Gestion/lista_empleados.html', {'empleados': empleados})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'Gestion/crear_empleado.html', {'form': form})

def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'Gestion/editar_empleado.html', {'form': form, 'empleado': empleado})

def borrar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'Gestion/borrar_empleado.html', {'empleado': empleado})


# VISTAS PARTES DE TRABAJO

def lista_partes(request):
    partes = Parte_Trabajo.objects.all().order_by('codigo')
    return render(request, 'Gestion/lista_partes.html', {'partes': partes})

def crear_parte(request):
    if request.method == 'POST':
        form = ParteTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_partes')
    else:
        form = ParteTrabajoForm()
    return render(request, 'Gestion/crear_parte.html', {'form': form})

def editar_parte(request, pk):
    parte = get_object_or_404(Parte_Trabajo, pk=pk)
    if request.method == 'POST':
        form = ParteTrabajoForm(request.POST, instance=parte)
        if form.is_valid():
            form.save()
            return redirect('lista_partes')
    else:
        form = ParteTrabajoForm(instance=parte)
    return render(request, 'Gestion/editar_parte.html', {'form': form, 'parte': parte})

def borrar_parte(request, pk):
    parte = get_object_or_404(Parte_Trabajo, pk=pk)
    if request.method == 'POST':
        parte.delete()
        return redirect('lista_partes')
    return render(request, 'Gestion/borrar_parte.html', {'parte': parte})

class MiPerfilAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
        })