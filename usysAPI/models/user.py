from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    #campos del modelo
    identification = models.CharField("codigo estudiante", unique = True,max_length = 12)
    first_name = models.CharField("nombre(s) estudiante",max_length = 30)
    last_name = models.CharField("apellido(s) estudiante",max_length = 30)
    
    #USERNAME_FIELD indica que campo se va a usar para el login
    USERNAME_FIELD = 'identification'
    
    #campos que se requieren para el login
    REQUIRED_FIELDS = ['first_name','last_name']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.last_name} - {self.first_name} - {self.email}'