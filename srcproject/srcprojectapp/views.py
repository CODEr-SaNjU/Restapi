import jwt
from .models import UserProfile,LeadGenerator
from rest_framework.response import Response
from .utils import otp_generator,send_mail_func
from django.utils.crypto import get_random_string
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import generics, request, serializers,  status, views
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import  AllowAny
from .serializers import UserChangePasswordSerializer, UserPasswordRestSerializer,LeadGeneratorSerializer, LeadUpdateGeneratorSerializer,UserProfileSerializer ,UserLoginSerializer
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from django.contrib import auth
from django.urls import reverse

#class based view 

class UserCreateApiView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
    
class UserLoginApiView(GenericAPIView):
    serializer_class  = UserLoginSerializer
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

def send_otp_forgot(email):
    if email:
        key = otp_generator()
        otp_key = str(key)
        user = get_object_or_404(UserProfile,email__iexact=email)
        if user.first_name:
            name = user.first_name
            print(name)
        else:
            name = email
            print(name)
        return otp_key
    else:
        return False

class UserPasswordRestApiView(GenericAPIView):
    serializer_class = UserPasswordRestSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email', '')
        if UserProfile.objects.filter(email=email).exists():
            otp = send_otp_forgot(email)
            subject = ('one time password ')
            message = ('this is message area here and otp is  {} '.format(otp))
            from_email = settings.EMAIL_HOST_USER
            to_email = (email,)
            send_mail_func(subject,message,from_email,to_email)
            messageSent = True
        else:
            return Response({'error':'Email is not found','status':status.HTTP_401_UNAUTHORIZED})

        return  Response({'success':'We have sent you a Otp to reset your password','status':status.HTTP_200_OK})



class LeadGeneratorViewset(viewsets.ViewSet):
    queryset = LeadGenerator.objects.all()
    serializer_class = LeadGeneratorSerializer

    @action(detail=True,methods=['GET'])
    def list(self,request):
        '''this will return list of all leads'''
        serializer_class =  LeadGeneratorSerializer(self.queryset, many=True)
        return Response(serializer_class.data)
        
    @action(detail=True,methods=['GET'])
    def retrieve(self, request, pk=None):
        '''this returns a single object'''
        leads = get_object_or_404(self.queryset,pk=pk)
        serializer_class = LeadGeneratorSerializer(leads)
        return Response(serializer_class.data)

    @action(detail=True,methods=['POST'])
    def create(self, request):
        '''this will create a lead '''
        serializer = LeadGeneratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)
        


    def partial_update(self, request, pk):
        leads = LeadGenerator.objects.get(pk=pk)
        serializer = LeadGeneratorSerializer(leads, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
 
        return Response(serializer.data)

    def update(self, request, pk):
        '''this will update leads'''
        leads = LeadGenerator.objects.get(pk=pk)
        serializer = LeadUpdateGeneratorSerializer(leads,data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        '''this will delete lead'''
        leads = LeadGenerator.objects.get(pk=pk)
        leads.delete()
        return Response({'Success':'Leads  is delete successfully'})


lead_list = LeadGeneratorViewset.as_view({'get': 'list'})
lead_partial_update = LeadGeneratorViewset.as_view({'patch':'partial_update'})
lead_update = LeadGeneratorViewset.as_view({'put':'update'})
lead_create = LeadGeneratorViewset.as_view({'post':'create'})
lead_detail = LeadGeneratorViewset.as_view({'get': 'retrieve'})
lead_delete = LeadGeneratorViewset.as_view({'delete':'destroy'})