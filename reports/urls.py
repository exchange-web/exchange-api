from django.urls import path
from .views import summary_report, client_report, operation_type_report, generate_report_xlsx

urlpatterns = [
    path('summary/', summary_report, name='summary_report'),
    path('client/<int:client_id>/', client_report, name='client_report'),
    path('operation_type/', operation_type_report, name='operation_type_report'),
    path('generate_report_xlsx/', generate_report_xlsx, name='generate_report_xlsx'),
]