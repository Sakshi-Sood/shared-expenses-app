from django.conf import settings
from django.db import models
from groups.models import Group


class Settlement(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="settlements"
    )

    payer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="settlements_paid"
    )

    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="settlements_received"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    currency = models.CharField(
        max_length=10,
        default="INR"
    )

    settlement_date = models.DateField()

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.payer} → {self.receiver}"