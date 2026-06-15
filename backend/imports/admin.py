from django.contrib import admin
from .models import ImportJob, Anomaly

admin.site.register(ImportJob)
admin.site.register(Anomaly)