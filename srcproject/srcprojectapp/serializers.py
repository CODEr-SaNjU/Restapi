from re import T
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = UserProfile
        fields = ['email','mob_number','first_name','last_name','user_type','password','password2']
        extra_kwargs = {
            'password':{'write_only': True}
        }
        
    def save(self):
        userprofile = UserProfile(
                    email = self.validated_data['email'],
                    mob_number = self.validated_data['mob_number'],
                    first_name = self.validated_data['first_name'],
                    last_name = self.validated_data['last_name']
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match.'})
        
        userprofile.set_password(password)
        userprofile.save()
        return userprofile


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    email   = serializers.EmailField(max_length=255)

    class Meta:
        model = UserProfile
        fields = ['email','password']
