from django.db import models

# Create your models here.

Matiers = (
    ('arabe','arabe'),
    ('math','math'),
    ('FR','FR'),
)

Cycles = [
    ('primaire','primaire'),
    ('secondaire', (
        ('collegial','collegial'),
        ('qualifiant','qualifiant'),
    )
    ),
]
class Prof(models.Model):  #table Prof
    nom = models.CharField(max_length=100) #colonne nom
    prenom = models.CharField(max_length=100) #colonne prenom
    num = models.IntegerField(default=1)
    matiere = models.CharField(max_length=25, choices=Matiers, default="")
    cycle = models.CharField(max_length=15, choices=Cycles)
    description = models.TextField(max_length=1000)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
    
        
