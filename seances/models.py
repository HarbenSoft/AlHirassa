from django.db import models

Matiers = (
    ('arabe','arabe'),
    ('math','math'),
    ('FR','FR'),
)
# Create your models here.
class Seance(models.Model):
    matiere = models.CharField(max_length=25, choices=Matiers)
    date =models.DateField()
    HeureDebut = models.TimeField()
    HeureFin = models.TimeField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.matiere