from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
# from django.utils.translation import gettext_lazy as _

from datetime import date

from .managers import CustomUserManager

class Alta_usuarios(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    dni = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True, db_column='activo', verbose_name='activo') # Es requerido por CustomUser
    empresa = models.ManyToManyField("empresa.Alta_empresas")
    # rol = models.OneToOneField("Roles", on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False, db_column='rol', verbose_name='rol') # Es requerido por CustomUser
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def baja_usuario(self):
        if not self.activo:
            return date.today() < self.fecha_baja

    def __str__(self):
        return self.email

class Roles(models.Model):
    rol_descripcion = models.CharField(max_length=255, blank=True, null=True)
    tipo_acceso_id = models.CharField(max_length=255, blank=False, null=False)
    menu_acceso = models.CharField(max_length=255, blank=True, null=True)

class Auditoria_usuarios(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    tipo_accion = models.CharField(max_length=255, blank=False, null=False)
    tabla_modificada = models.CharField(max_length=255, blank=True, null=True)
    registro_modificado = models.CharField(max_length=255, blank=True, null=True)