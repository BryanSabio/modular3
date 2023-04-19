# Serializers es para las tranferencias de servidor a cliente y viseversa.

from rest_framework import serializers
from api.models import ProductoPequeno, ProductoMediano, ProductoGrande, ProductoGigante
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProductopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoPequeno
        fields = '__all__'
        read_only_fields = ('created_at',)

class ProductomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoMediano
        fields = '__all__'
        read_only_fields = ('created_at',)

class ProductogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoGrande
        fields = '__all__'
        read_only_fields = ('created_at',)

class ProductoGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoGigante
        fields = '__all__'
        read_only_fields = ('created_at',)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'groups', 'email']
        #esconder password
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user