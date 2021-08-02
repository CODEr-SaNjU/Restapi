import jwt
from .models import UserProfile
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .serializers import UserProfileSerializer ,LoginSerializer
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from django.contrib import auth
class UserCreateApiView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)


class UserLoginApiView(GenericAPIView):
    serializer_class  = LoginSerializer
    def post(self,request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(email = email,password = password)

        if user:
            auth_token = jwt.encode({'email': user.email},settings.JWT_SECRET_KEY)


            serializer = UserProfileSerializer(user)
            data = {
                "user":serializer.data,
                'token': auth_token
            }

            return Response(data, status= status.HTTP_200_OK)

            #sen res
        
        return Response({'details':'Invalid credentials'},status= status.HTTP_401_UNAUTHORIZED)