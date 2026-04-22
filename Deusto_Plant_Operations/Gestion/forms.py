from django import forms
from .models import Empleado, Turno, ParteTrabajo

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'franja': forms.Select(attrs={'class': 'form-select'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ParteTrabajoForm(forms.ModelForm):
    class Meta:
        model = ParteTrabajo
        fields = '__all__'
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'turno': forms.Select(attrs={'class': 'form-select'}),
            'tarea': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'incidencias': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }