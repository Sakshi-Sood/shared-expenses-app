from django.db import models


class ImportJob(models.Model):

    STATUS_CHOICES = [
        ("uploaded", "Uploaded"),
        ("analyzed", "Analyzed"),
        ("approved", "Approved"),
        ("imported", "Imported"),
    ]

    filename = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="uploaded"
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    completed_at = models.DateTimeField(
        null=True,
        blank=True
    )


class Anomaly(models.Model):

    import_job = models.ForeignKey(
        ImportJob,
        on_delete=models.CASCADE,
        related_name="anomalies"
    )

    row_number = models.IntegerField()

    anomaly_type = models.CharField(max_length=100)

    description = models.TextField()

    suggested_action = models.TextField()

    user_decision = models.CharField(
        max_length=100,
        blank=True
    )

    resolved = models.BooleanField(
        default=False
    )