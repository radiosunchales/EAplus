from django.db import models

class Alta_establecimientos(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    abreviatura = models.CharField(max_length=255, blank=False, null=False)
    establecimiento_tipo_id = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)
    provincia = models.CharField(max_length=255, blank=True, null=True)
    pais = models.CharField(max_length=255, blank=True, null=True)
    latitud = models.CharField(max_length=255, blank=True, null=True)
    longitud = models.CharField(max_length=255, blank=True, null=True)
    zona_id = models.CharField(max_length=255, blank=True, null=True)
    observaciones = models.TextField(max_length=255, blank=True, null=True)
    contacto = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField("usuario.Alta_usuarios", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre