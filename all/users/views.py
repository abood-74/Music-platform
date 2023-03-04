from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer

class UserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            if request.user == user: # check if user making the request is the same as the user in the URL
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'error': 'Unauthorized user.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if request.user == user: # check if user making the request is the same as the user in the URL
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'error': 'Unauthorized user.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
