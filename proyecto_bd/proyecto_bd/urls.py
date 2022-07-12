from django.contrib import admin
from django.urls import path
from appgestion import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_todo/',views.listar_todo),
    path('listar_todo_persona/',views.listar_todo_persona),
    path('ingresar_persona/', views.ingresar_persona),
    path('ingreso_persona/',views.ingreso_persona),    
    path('busqueda_persona/',views.busqueda_persona),
    path('buscar/',views.buscar),
    path('eliminar_persona/',views.eliminar_persona),
    path('eliminacion_persona/',views.eliminacion_persona),   
    path('modificar_persona/',views.modificar_persona),
    path('modificar/',views.modificar),

    path('',views.index),
    path('index/',views.index),

    path('ingresar_vacuna/',views.ingresar_vacuna),
    path('ingreso_vacuna/',views.ingreso_vacuna),
    path('busqueda_vacuna/',views.busqueda_vacuna),
    path('buscar_vacuna/',views.buscar_vacuna),
    path('eliminar_vacuna/',views.eliminar_vacuna),
    path('eliminacion_vacuna/',views.eliminacion_vacuna), 
    path('modificarvacuna/',views.modificarvacuna),
    path('modificar_vacuna/',views.modificar_vacuna),
    path('listar_todo_vacunas/',views.listar_todo_vacunas),
    path('listar_todo_vac/',views.listar_todo_vac),
]

