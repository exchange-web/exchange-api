from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsAdminUser, IsOperatorUser
from .models import DataEntry
from .serializers import DataEntrySerializer

class DataEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser | IsOperatorUser]
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer

    def get_permissions(self):
        if self.action == 'destroy':
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated, IsAdminUser | IsOperatorUser]
        return super().get_permissions()