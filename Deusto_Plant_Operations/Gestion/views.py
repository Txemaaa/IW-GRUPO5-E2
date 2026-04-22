from django.shortcuts import render

from .models import Turno, Parte_Trabajo, Empleado
def turno_list(request):
    turnos = Turno.objects.all()
    return render(request, 'turno_list.html', {'turnos': turnos})

def parte_trabajo_list(request):
    partes_trabajo = Parte_Trabajo.objects.all()
    return render(request, 'parte_trabajo_list.html', {'partes_trabajo': partes_trabajo})

def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado_list.html', {'empleados': empleados})
