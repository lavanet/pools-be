from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class Dated(models.Model):
    dt_created = models.DateTimeField(
        verbose_name=_('date created'),
        default=now,
        db_index=True,
        blank=True,
    )

    class Meta:
        abstract = True


class UpDated(Dated):
    dt_updated = models.DateTimeField(
        verbose_name=_('date updated'),
        db_index=True,
        auto_now=True,
    )

    class Meta:
        abstract = True
