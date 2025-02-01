from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsAdminUser, IsOperatorUser
from currencies.models import Currency
from currencies.serializers import CurrencySerializer

class CurrencyByCodeView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser | IsOperatorUser]

    def get(self, request, code):
        currency = get_object_or_404(Currency, code=code)
        serializer = CurrencySerializer(currency)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, code):
        currency = get_object_or_404(Currency, code=code)
        serializer = CurrencySerializer(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code):
        currency = get_object_or_404(Currency, code=code)
        self.check_object_permissions(request, currency)
        currency.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def check_object_permissions(self, request, obj):
        if request.method == 'DELETE' and not request.user.is_admin:
            self.permission_denied(request, message="You do not have permission to delete this object.")
        super().check_object_permissions(request, obj)