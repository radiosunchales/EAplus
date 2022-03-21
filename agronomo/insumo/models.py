from django.db import models

class Tipo_erogaciones(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    abreviatura = models.CharField(max_length=255, blank=False, null=False)
    user = models.OneToOneField("usuario.Alta_usuarios", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

class Unidades(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField("usuario.Alta_usuarios", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

class Rubros(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField("usuario.Alta_usuarios", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

class Familias(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField("usuario.Alta_usuarios", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

class Subfamilias(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField("usuario.Alta_usuarios", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

class Alta_insumos(models.Model):
    nombre = models.CharField(max_length=255, blank=False, null=False)
    abreviatura = models.CharField(max_length=255, blank=False, null=False)
    codigo_externo = models.CharField(max_length=255, blank=True, null=True)
    lote_control = models.BooleanField(blank=True, null=True)
    lote_numero = models.IntegerField(blank=True, null=True)
    vencimiento_control = models.BooleanField(blank=True, null=True)
    vencimiento_fecha = models.DateTimeField(blank=True, null=True)
    reposicion_control = models.BooleanField(blank=True, null=True)
    reposicion_cantidad = models.IntegerField(blank=True, null=True)
    reposicion_alerta = models.CharField(max_length=255, blank=True, null=True)
    tipo_erogacione = models.OneToOneField("Tipo_erogaciones", on_delete=models.PROTECT)
    unidade = models.OneToOneField("Unidades", on_delete=models.PROTECT)
    rubro = models.OneToOneField("Rubros", on_delete=models.PROTECT)
    familia = models.OneToOneField("Familias", on_delete=models.PROTECT)
    subfamilia = models.OneToOneField("Subfamilias", on_delete=models.PROTECT)
    user = models.OneToOneField("usuario.Alta_usuarios", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre