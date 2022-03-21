from django.db import models

class Alta_facturacion(models.Model):
    tarjeta_emisor_id = models.CharField(max_length=255, blank=True, null=True)
    nro_tarjeta = models.IntegerField(blank=True, null=True)
    vto_fecha = models.DateField(blank=True, null=True)
    cod_verificacion = models.IntegerField(blank=True, null=True)
    fecha_alta = models.DateTimeField(auto_now_add=True)
    fecha_baja = models.DateTimeField(blank=True, null=True) # Ver cuando se da de baja la facturacion

    def __str__(self):
        return self.nro_tarjeta