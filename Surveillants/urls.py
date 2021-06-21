from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Surveillants_list),
    path('<int:id>', views.Surveillants_details),

]

