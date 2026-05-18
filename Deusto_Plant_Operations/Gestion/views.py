from urllib import request
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Turno, Empleado, Parte_Trabajo
from .forms import TurnoForm, EmpleadoForm, ParteTrabajoForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'Gestion/index.html')

# VISTAS TURNOS

@login_required(login_url='/login/')
def lista_turnos(request):
    todos_los_turnos = Turno.objects.all().order_by('fecha')
    paginador = Paginator(todos_los_turnos, 5)
    pagina = request.GET.get('page')
    turnos = paginador.get_page(pagina)
    return render(request, 'Gestion/lista_turnos.html', {'turnos': turnos})

@login_required(login_url='/login/')
def crear_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_turnos')
    else:
        form = TurnoForm()
    return render(request, 'Gestion/crear_turno.html', {'form': form})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def borrar_turno(request, pk):
    turno = get_object_or_404(Turno, pk=pk)
    if request.method == 'POST':
        turno.delete()
        return redirect('lista_turnos')
    return render(request, 'Gestion/borrar_turno.html', {'turno': turno})


# VISTAS EMPLEADOS

@login_required(login_url='/login/')
def lista_empleados(request):
    todos_los_empleados = Empleado.objects.all().order_by('apellido')
    paginador = Paginator(todos_los_empleados, 5)
    pagina = request.GET.get('page')
    empleados = paginador.get_page(pagina)
    return render(request, 'Gestion/lista_empleados.html', {'empleados': empleados})

@login_required(login_url='/login/')
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'Gestion/crear_empleado.html', {'form': form})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def borrar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')
    return render(request, 'Gestion/borrar_empleado.html', {'empleado': empleado})


# VISTAS PARTES DE TRABAJO

@login_required(login_url='/login/')
def lista_partes(request):
    partes = Parte_Trabajo.objects.all().order_by('codigo')
    empleado_busqueda = request.GET.get('empleado', '')
    estado_busqueda = request.GET.get('estado', '')
    if empleado_busqueda:
        partes = partes.filter(empleado__nombre__icontains=empleado_busqueda)
    if estado_busqueda:
        partes = partes.filter(estado=estado_busqueda)
    paginador = Paginator(partes, 5)
    pagina = request.GET.get('page')
    partes = paginador.get_page(pagina)
    return render(request, 'Gestion/lista_partes.html', {
        'partes': partes,
        'empleado_busqueda': empleado_busqueda,
        'estado_busqueda': estado_busqueda,
    })

@login_required(login_url='/login/')
def crear_parte(request):
    if request.method == 'POST':
        form = ParteTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_partes')
    else:
        form = ParteTrabajoForm()
    return render(request, 'Gestion/crear_parte.html', {'form': form})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
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

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_turnos')
        else:
            return render(request, 'Gestion/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'Gestion/login.html')