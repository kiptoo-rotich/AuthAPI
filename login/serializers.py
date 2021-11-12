from django.db.models import fields
from rest_framework import serializers
from .models import Register,Login

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields='__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields='__all__'