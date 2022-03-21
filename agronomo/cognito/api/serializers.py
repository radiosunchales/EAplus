from rest_framework import serializers

from usuario.models import Alta_usuarios

class Alta_usuarios_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Alta_usuarios
        fields = ['email', 'nombre'] # '__all__'