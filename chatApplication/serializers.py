from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        feilds = ['username', 'email', 'password']