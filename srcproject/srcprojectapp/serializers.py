from rest_framework import serializers
from .models import UserProfile,LeadGenerator


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


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    email   = serializers.EmailField(max_length=255)

    class Meta:
        model = UserProfile
        fields = ['email','password']


class UserChangePasswordSerializer(serializers.Serializer):
    password_1 = serializers.CharField(required=True)
    password_2 = serializers.CharField(required=True)


class UserPasswordRestSerializer(serializers.Serializer):
    """
    Used for resetting password who forget their password via otp varification
    """
    email = serializers.EmailField(min_length=10,required=True)




class LeadGeneratorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LeadGenerator
        fields = '__all__'
class LeadUpdateGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadGenerator
        fields = ['lead_name','lead_source','lead_user_email']

