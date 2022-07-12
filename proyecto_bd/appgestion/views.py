from django.shortcuts import render
from appgestion.models import Persona
from appgestion.models import Vacuna
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def ingresar_persona(request):
    return render(request,"ingresar_persona.html")

def index(request):
    return render(request,"index.html")

def busqueda_persona(request):
    return render(request,"busqueda_persona.html") 

def listar_todo(request):
    return render(request,"listar_todo.html")

def eliminar_persona(request):
    return render(request,"eliminar_persona.html")

def modificar_persona(request):
    return render(request,"modificar_persona.html")

def ingresar_vacuna(request):
    return render(request,"ingresar_vacuna.html")

def busqueda_vacuna(request):
    return render(request,"busqueda_vacuna.html") 

def eliminar_vacuna(request):
    return render(request,"eliminar_vacuna.html")

def modificarvacuna(request):
    return render(request,"modificar_vacuna.html")

def listar_todo_vacunas(request):
    return render(request,"listar_todo_vacunas.html")

##VIEWS DE PERSONAS##

def listar_todo_persona(request):
    datos = Persona.objects.all()  
    return render(request,"listar_todo.html",{'personas':datos})
    
def ingreso_persona(request):
    rut=request.GET["txt_rut"]
    nombre=request.GET["txt_nombre"]
    apellido_paterno=request.GET["txt_appaterno"]
    apellido_materno=request.GET["txt_apmaterno"]
    edad=request.GET["txt_edad"]
    vacuna=request.GET["txt_vacuna"]
    fecha=request.GET["txt_fecha"]
    if len(rut)>0 and len(nombre)>0 and len(apellido_paterno)>0 and len(apellido_materno)>0 and len(edad)>0 and len(vacuna)>0 and len(fecha)>0:
        per=Persona(rut=rut,nombre=nombre,apellido_paterno=apellido_paterno,apellido_materno=apellido_materno,edad=edad,vacuna=vacuna,fecha=fecha)  
        per.save()
        return render(request,"index.html")
    else:
        mensaje="Error al ingresar persona"
    return HttpResponseRedirect('../index/')

def buscar(request):
    if request.GET["txt_rut"]:
        rut = request.GET["txt_rut"]
        personas = Persona.objects.filter(rut__icontains=rut)
        return render(request,"listar.html",{"personas":personas,"query":rut})
    else:
        mensaje = "Debe ingresar el RUT de la persona a buscar"
    return HttpResponseRedirect('../index/')


def eliminacion_persona(request):
    if request.GET["txt_rut"]:
        rut_recibido = request.GET["txt_rut"]
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            per=Persona.objects.get(rut=rut_recibido)
            per.delete()
            return render(request,"index.html")
        else:
            mensaje = "Persona No Eliminada"
    else:
        mensaje = "Ingrese RUT para Eliminar"
    return HttpResponseRedirect('../index/')

def modificar(request):
    if request.GET["txt_rut"]:
        rut_recibido = request.GET["txt_rut"]
        vacuna_recibida = request.GET["txt_vacuna"]
        fecha_recibida = request.GET["txt_fecha"]
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            per=Persona.objects.get(rut=rut_recibido)
            per.vacuna = vacuna_recibida
            per.fecha = fecha_recibida
            per.save()
            return render(request,"index.html")           
        else:
            mensaje = "No existe registro de persona para modificar"           
    else:
        mensaje = "Debe ingresar un RUT para modificar"
    return HttpResponseRedirect('../index/')

##VIEWS DE VACUNAS##
def ingreso_vacuna(request):
    id=request.GET["txt_id"]
    marca=request.GET["txt_marca"]
    laboratorio=request.GET["txt_laboratorio"]
    stock=request.GET["txt_stock"]
    fecha_elab=request.GET["txt_fechaelab"]
    fecha_ven=request.GET["txt_fechaven"]
    if len(id)>0 and len(marca)>0 and len(laboratorio)>0 and len(stock)>0 and len(fecha_elab)>0 and len(fecha_ven)>0:
        vac=Vacuna(id=id,marca=marca,laboratorio=laboratorio,stock=stock,fecha_elab=fecha_elab,fecha_ven=fecha_ven)  
        vac.save()
        return render(request,"index.html")
    else:
        mensaje="Error al ingresar vacuna"
    return HttpResponseRedirect('../index/')

def buscar_vacuna(request):
    if request.GET["txt_marca"]:
        marca = request.GET["txt_marca"]
        vacunas = Vacuna.objects.filter(marca__icontains=marca)
        return render(request,"listar_vacuna.html",{"vacunas":vacunas,"query":marca})
    else:
        mensaje = "Debe ingresar la Marca de la vacuna a buscar"
    return HttpResponseRedirect('../index/')

def eliminacion_vacuna(request):
    if request.GET["txt_id"]:
        id_recibida = request.GET["txt_id"]
        vacuna = Vacuna.objects.filter(id=id_recibida)
        if vacuna:
            vac=Vacuna.objects.get(id=id_recibida)
            vac.delete()
            return render(request,"index.html")
        else:
            mensaje = "Vacuna no Eliminada"
    else:
        mensaje = "Ingrese Marca para Eliminar"
    return HttpResponseRedirect('../index/')

def modificar_vacuna(request):
    if request.GET["txt_id"]:
        id_recibida = request.GET["txt_id"]
        stock_recibido = request.GET["txt_stock"]
        fechaelab_recibida = request.GET["txt_fechaelab"]
        fechaven_recibida = request.GET["txt_fechaven"]
        vacuna = Vacuna.objects.filter(id=id_recibida)
        if vacuna:
            vac=Vacuna.objects.get(id=id_recibida)
            vac.stock = stock_recibido
            vac.fecha_elab = fechaelab_recibida
            vac.fecha_ven = fechaven_recibida
            vac.save()
            return render(request,"index.html")           
        else:
            mensaje = "No existe registro de vacunas para modificar"           
    else:
        mensaje = "Debe ingresar una Marca para modificar"
    return HttpResponseRedirect('../index/')

def listar_todo_vac(request):
    info = Vacuna.objects.all()  
    return render(request,"listar_todo_vacunas.html",{'vacunas':info})