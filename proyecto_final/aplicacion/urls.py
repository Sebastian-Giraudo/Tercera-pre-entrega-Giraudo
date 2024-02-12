from django.urls import path, include
from .views import *

urlpatterns = [    
    path('', home, name="1home"),
    
    path('consultorios/' , consultorios , name="consultorios"),
    path('especialidades/' , especialidades , name="especialidades"),
    path('profesionales/' , profesionales , name="profesionales"),
        
    #---------------------------------------------------------------------------------------------- 
     
    path('consultorio_form/' , consultorioForm , name="consultorio_form"),
    path('especialidad_form/' , especialidadForm , name="especialidad_form"),
    path('profesional_form/' , profesionalForm , name="profesional_form"),
        
    #----------------------------------------------------------------------------------------------    
      
    path('buscar/' , buscar , name="buscar"), 
    path('buscarConsultorio/' , buscarConsultorio , name="buscarConsultorio"),  
    path('buscarProfesional/' , buscarProfesional , name="buscarProfesional"),
    path('buscarEspecialidad/' , buscarEspecialidad , name="buscarEspecialidad"),
]