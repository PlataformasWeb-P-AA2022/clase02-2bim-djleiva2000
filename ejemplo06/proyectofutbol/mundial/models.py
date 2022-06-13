from django.db import models

# Create your models here.

class Estadio(models.Model):
    nombre = models.CharField(max_length=30)
    capacidad = models.IntegerField
   

    def __str__(self):
        return "%s - %s - %s - edad: %d" % (self.nombre, 
                self.capacidad)
                
class Equipo (models.Model):
    """
    """
    sigla = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    sobrenombre = models.CharField(max_length = 30)

    def __str__(self):
        return "%s - %s - %s"%(self.sigla,self.nombre,self.sobrenombre)







             