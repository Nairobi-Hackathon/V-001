from django import forms
from .models import AuditReport

class AuditReportForm(forms.ModelForm):
    class Meta:
        model = AuditReport
        fields = ['title', 'date', 'status', 'report']
