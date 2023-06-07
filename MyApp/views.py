from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserProfileSerializer,PostSerializer
from .models import UserProfile,Post


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
class UserProfileViewSet(viewsets.ViewSet):
    def list(self,request):
        data=UserProfile.objects.all()
        serializer_data=UserProfileSerializer(data,many=True)
        return Response(serializer_data.data)
    
    def retrieve(self,request,pk):
        try:
            data=UserProfile.objects.get(pk=pk)
        except:
            return Response("NOT FOUND")
        serialiser_data=UserProfileSerializer(data)
        return Response(serialiser_data.data)
    
    def create(self,request):
        serializer_data=UserProfileSerializer(data=request.data)
        if (serializer_data.is_valid()):
            serializer_data.save()
            return Response(serializer_data.data)
        return Response(serializer_data.errors)
    
    def destroy(self,request,pk):
        serializer_data=UserProfile.objects.get(pk=pk)
        serializer_data.delete()
        return Response("DATAA DELETED")
    
    def update(self,request,pk):
        data=UserProfile.objects.get(pk=pk)
        serializer_data=UserProfileSerializer(data,data=request.data)
        if (serializer_data.is_valid()):
            serializer_data.save()
            return Response(serializer_data.data)
        return Response(serializer_data.errors)
    


class PostViewSet(viewsets.ViewSet):
    #this can be un-commented to activate token authentication
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    def list(self,request):
        
        data=Post.objects.all()
        serializer=PostSerializer(data,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk):
        try:
            data=Post.objects.get(pk=pk)
            
        except:
            return Response("DOES NOT EXIST")
        serializer=PostSerializer(data)
        return Response(serializer.data)
    
    def update(self,request,pk):
        if request.user.is_authenticated:
            data=Post.objects.get(pk=pk)
            serializer=PostSerializer(data,data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("PERMISSION DENIED")

    def destroy(self,request,pk):
        
        if request.user.is_authenticated:
            data=Post.objects.get(pk=pk)
            data.delete()
            return Response("DELETED !!")
        return Response("PERMISSION DENIED")
    
    def create(self,request):
        if request.user.is_authenticated:
            serializer=PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("PERMISSION DENIED")

