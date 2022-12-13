from django.db import models

# Create your models here.
class Familiar (models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()
    edad=models.IntegerField()

    def __str__(self) -> str:
        return " ".join([self.nombre, str(self.fecha), str(self.edad)])