from django.db import models

# Create your models here.
class Salle(models.Model):
    nom = models.CharField(max_length=50) #colonne nom

    def __str__(self):
        return self.nom