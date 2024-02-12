from django import forms

#----------------------------------------------------------------------------------------------
class ConsultorioForm(forms.Form):    
    nombre = forms.CharField(max_length=50, required=True)
    direccion = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)

#----------------------------------------------------------------------------------------------
    
class ProfesionalForm(forms.Form):    
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    profesion = forms.CharField(max_length=50, required=True)

#----------------------------------------------------------------------------------------------    
    
class EspecialidadForm(forms.Form):    
    nombre = forms.CharField(max_length=50, required=True)
    consultorio = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)

#----------------------------------------------------------------------------------------------  
    

  