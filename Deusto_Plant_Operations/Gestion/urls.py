from django.urls import path
from . import views
from . import views



urlpatterns = [
    path('', views.inicio, name='inicio'),

    ## Rutas para Turnos
    path('turnos/', views.lista_turnos, name='lista_turnos'),
    path('turnos/nuevo/', views.crear_turno, name='crear_turno'),
    path('turnos/editar/<int:pk>/', views.editar_turno, name='editar_turno'),
    path('turnos/borrar/<int:pk>/', views.borrar_turno, name='borrar_turno'),

    # Rutas para Empleados
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/nuevo/', views.crear_empleado, name='crear_empleado'),
    path('empleados/editar/<int:pk>/', views.editar_empleado, name='editar_empleado'),
    path('empleados/borrar/<int:pk>/', views.borrar_empleado, name='borrar_empleado'),

    # Rutas para Partes de Trabajo
    path('partes/', views.lista_partes, name='lista_partes'),
    path('partes/nuevo/', views.crear_parte, name='crear_parte'),
    path('partes/editar/<int:pk>/', views.editar_parte, name='editar_parte'),
    path('partes/borrar/<int:pk>/', views.borrar_parte, name='borrar_parte'),

    # Ruta para el perfil del usuario autenticado
    path('api/me/', views.MiPerfilAPIView.as_view(), name='api_me'),
    path('login/', views.login_view, name='login'),
]