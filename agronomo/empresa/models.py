from django.db import models

class Alta_empresas(models.Model):
    # id = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=255, blank=False, null=False)
    direccion_calle = models.CharField(max_length=255, blank=False, null=False)
    direccion_nro = models.CharField(max_length=255, blank=False, null=False)
    direccion_localidad = models.CharField(max_length=255, blank=False, null=False)
    direccion_provincia = models.CharField(max_length=255, blank=False, null=False)
    direccion_pais = models.CharField(max_length=255, blank=False, null=False)
    direccion_cod_postal = models.CharField(max_length=255, blank=False, null=False)
    cuit = models.IntegerField(blank=True, null=True)
    cond_IVA_id = models.CharField(max_length=255, blank=True, null=True)
    rubro = models.ForeignKey("insumo.Rubros", on_delete=models.PROTECT)
    fecha_cierre = models.DateField(blank=False, null=False)
    moneda_primaria_id = models.CharField(max_length=255, blank=True, null=True)
    moneda_secundaria_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.razon_social

class Inquilinos(models.Model):
    # nombre = models.CharField(max_length=255, blank=True, null=True)
    # uri_rds = models.CharField(max_length=255, blank=True, null=True)
    # uri_bucket_s3 = models.CharField(max_length=255, blank=True, null=True)
    # uri_API_gateway = models.CharField(max_length=255, blank=True, null=True)
    # dominio = models.CharField(max_length=255, blank=True, null=True)
    # modulos_API = models.CharField(max_length=255, blank=True, null=True)
    # billing = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    empresas = models.CharField(max_length=255, blank=True, null=True)
    usuarios = models.CharField(max_length=255, blank=True, null=True)
    accesos_por_rol = models.CharField(max_length=255, blank=True, null=True)