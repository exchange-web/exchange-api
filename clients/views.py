# myapp/views.py

from rest_framework import generics
from common.permissions import HasAPIKey
from .models import Client
from .serializers import ClientSerializer
from common.authentication import APIKeyAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ClientListCreate(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [HasAPIKey]

class ClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [HasAPIKey]

class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [HasAPIKey]

    def create(self, request, *args, **kwargs):
        client_id = request.data.get('id')
        while Client.objects.filter(id=client_id).exists():
            client = Client.objects.get(id=client_id)
            client.pk = None 
            client.save()
            client_id = client.id 
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)