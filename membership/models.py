import uuid

from datetime import datetime, timedelta
from django.db import models

from product.models import Product


class Membership(models.Model):
    product = models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
        )
    membership_number = models.UUIDField(
        default=uuid.uuid4().hex.upper()[:8],
        unique=True,
        editable=False
        )
    active = models.BooleanField(
        default=False,
        null=True,
        blank=True
        )
    date_activated = models.DateField(
        auto_now=True
        )
    expiry_date = models.DateTimeField(
        null=True,
        blank=True
        )

    def save(self, *args, **kwargs):
        if self.date_activated and not self.expiry_date:
            date_activated_days = self.date_activated.timedelta().days()
            self.expiry_date = datetime.now() + timedelta(
                days=date_activated_days)
        super(Membership, self).save(*args, **kwargs)
