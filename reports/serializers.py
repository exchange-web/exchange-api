from rest_framework import serializers
from data_entries.models import DataEntry
from clients.models import Client
from currencies.models import Currency

class SummaryReportSerializer(serializers.Serializer):
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    average_rate = serializers.DecimalField(max_digits=10, decimal_places=4)
    client = serializers.CharField()
    currency_pair = serializers.CharField()

class ClientReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntry
        fields = '__all__'

class OperationTypeReportSerializer(serializers.Serializer):
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    average_rate = serializers.DecimalField(max_digits=10, decimal_places=4)
    transaction_type = serializers.CharField()
    currency_pair = serializers.CharField()