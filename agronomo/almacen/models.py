from django.db import models

class Alta_almacen(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    abreviatura = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.TextField(max_length=255, blank=True, null=True)
    establecimiento = models.OneToOneField("establecimiento.Alta_establecimientos", on_delete=models.PROTECT)
    almacenes_tipo_id = models.CharField(max_length=255, blank=True, null=True)
    geoposicion = models.CharField(max_length=255, blank=True, null=True)
    observaciones = models.TextField(max_length=255, blank=True, null=True)
    user = models.OneToOneField("usuario.Alta_usuarios", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre