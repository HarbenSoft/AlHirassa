from django.contrib import admin

# Register your models here.

from .models import Surveillants, Matiere

admin.site.register(Surveillants)
admin.site.register(Matiere)
