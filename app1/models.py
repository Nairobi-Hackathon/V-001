from django.db import models
from django.utils import timezone

class AuditReport(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    status_choices = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('violation_detected', 'Violation Detected'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='in_progress')
    report = models.TextField()

    def __str__(self):
        return self.title

class ComplianceStatus(models.Model):
    compliance_rate = models.FloatField(default=0.0)
    open_audits = models.IntegerField(default=0)
    violations_detected = models.IntegerField(default=0)

    def __str__(self):
        return f"Compliance: {self.compliance_rate}%"

