from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import serializers

class LogoutSerializer(serializers.Serializer):
    pass
class StatusSerializer(serializers.Serializer):
    pass

class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Criptografa a senha
        user.save()
        return user

class AutenticarSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()