from django.db import models

# Create your models here.


Cycles = [
    ('primaire','primaire'),
    ('secondaire', (
        ('collegial','collegial'),
        ('qualifiant','qualifiant'),
    )
    ),
]


            

class Surveillants(models.Model):  #table Surveillants
    nom = models.CharField(max_length=100) #colonne nom
    prenom = models.CharField(max_length=100) #colonne prenom
    num = models.IntegerField()
    matiere = models.ForeignKey('Matiere',on_delete = models.CASCADE)
    cycle = models.CharField(max_length=15, choices=Cycles)
    description = models.TextField(max_length=1000)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Matiere(models.Model):
    designation = models.CharField(max_length=30)
    
    def __str__(self):
        return self.designation