from django.shortcuts import render
from .models import AuditReport, ComplianceStatus
# Create your views here.

# index page
def index(request):
    return render(request, "app1/index.html")


def dashboard(request):
      # Fetch audit reports and compliance status from the database
    audits = AuditReport.objects.all().order_by('-date')
    compliance_status = ComplianceStatus.objects.last()  # Assuming there's only one status record

    context = {
        'audits': audits,
        'compliance_status': compliance_status,
    }
    return render(request, "app1/dashboard.html")


def register(request):
    return render(request, 'app1/register.html')