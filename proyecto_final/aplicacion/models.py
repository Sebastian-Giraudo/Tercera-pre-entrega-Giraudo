from django.db import models


#----------------------------------------------------------------------------------------------

class Consultorio(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.telefono}, {self.email}"
    
    class Meta:        
        ordering = ['nombre']

#---------------------------------------------------------------------------------------------- 

class Especialidad(models.Model):
    nombre = models.CharField(max_length=40)
    consultorio = models.CharField(max_length=40)
    telefono = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.consultorio}, {self.telefono}"

    class Meta: 
        verbose_name = "especialidad"
        verbose_name_plural = "Especialidades"
        ordering = ['nombre']
    
#----------------------------------------------------------------------------------------------    
class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.profesion}"
    
    class Meta: 
        verbose_name = "profesional"
        verbose_name_plural = "Profesionales"
        ordering = ['profesion', 'apellido']

#----------------------------------------------------------------------------------------------


