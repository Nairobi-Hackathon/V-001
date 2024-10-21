from django.contrib import admin
from .models import AuditReport, ComplianceStatus

admin.site.register(AuditReport)
admin.site.register(ComplianceStatus)

