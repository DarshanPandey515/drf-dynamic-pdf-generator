from rest_framework import serializers
from myapp.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password',)

    def create(self, validated_data):
        user = User.objects.create_user(username = validated_data['username'], password = validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class EmplyoeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'