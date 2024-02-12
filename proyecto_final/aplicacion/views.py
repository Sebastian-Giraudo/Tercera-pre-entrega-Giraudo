from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

#----------------------------------------------------------------------------------------------

def home(request):
    return render(request, "aplicacion/1home.html")

def consultorios(request):
    contexto = {'consultorios': Consultorio.objects.all()}
    return render(request, "aplicacion/consultorios.html", contexto)

def especialidades(request):
    contexto = {'especialidades': Especialidad.objects.all()}
    return render(request, "aplicacion/especialidades.html", contexto)

def profesionales(request):
    contexto = {'profesionales': Profesional.objects.all()}
    return render(request, "aplicacion/profesionales.html", contexto)

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

def consultorioForm(request):
    if request.method == "POST":
        miForm = ConsultorioForm(request.POST)
        if miForm.is_valid():
            consultorio_nombre = miForm.cleaned_data.get("nombre")
            consultorio_direccion = miForm.cleaned_data.get("direccion")
            consultorio_telefono = miForm.cleaned_data.get("telefono")
            consultorio_email = miForm.cleaned_data.get("email")
            consultorio = Consultorio(nombre=consultorio_nombre , direccion=consultorio_direccion , telefono=consultorio_telefono , email=consultorio_email)
            consultorio.save()
            return render(request, "aplicacion/1home.html")
    else:
        miForm = ConsultorioForm()
    
    return render(request, "aplicacion/consultorioForm.html" , {"form": miForm })
#----------------------------------------------------------------------------------------------

def especialidadForm(request):
    if request.method == "POST":
        miForm = EspecialidadForm(request.POST)
        if miForm.is_valid():
            especialidad_nombre = miForm.cleaned_data.get("nombre")
            especialidad_consultorio = miForm.cleaned_data.get("consultorio")
            especialidad_telefono = miForm.cleaned_data.get("telefono")            
            especialidad = Especialidad(nombre=especialidad_nombre , consultorio=especialidad_consultorio , telefono=especialidad_telefono)
            especialidad.save()
            return render(request, "aplicacion/1home.html")
    else:
        miForm = EspecialidadForm()
    
    return render(request, "aplicacion/especialidadForm.html" , {"form": miForm })

#----------------------------------------------------------------------------------------------

def profesionalForm(request):
    if request.method == "POST":
        miForm = ProfesionalForm(request.POST)
        if miForm.is_valid():
            profesional_nombre = miForm.cleaned_data.get("nombre")
            profesional_apellido = miForm.cleaned_data.get("apellido")
            profesional_profesion = miForm.cleaned_data.get("profesion")            
            profesional = Profesional(apellido=profesional_apellido , nombre=profesional_nombre , profesion=profesional_profesion)
            profesional.save()
            return render(request, "aplicacion/1home.html")
    else:
        miForm = ProfesionalForm()
    
    return render(request, "aplicacion/profesionalForm.html" , {"form": miForm })

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarConsultorio(request):
    if request.GET["buscar"]: 
        patron = request.GET["buscar"]
        consultorios = Consultorio.objects.filter(nombre__icontains=patron) 
        contexto = {"consultorios": consultorios }
        return render(request, "aplicacion/consultorios.html" , contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

#----------------------------------------------------------------------------------------------

def buscarEspecialidad(request):
    if request.GET["buscar"]: 
        patron = request.GET["buscar"]
        especialidades = Especialidad.objects.filter(nombre__icontains=patron) 
        contexto = {"especialidades": especialidades }
        return render(request, "aplicacion/especialidades.html" , contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

#----------------------------------------------------------------------------------------------

def buscarProfesional(request):
    if request.GET["buscar"]: 
        patron = request.GET["buscar"]
        profesionales = Profesional.objects.filter(nombre__icontains=patron) 
        contexto = {"profesionales": profesionales }
        return render(request, "aplicacion/profesionales.html" , contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

#----------------------------------------------------------------------------------------------
