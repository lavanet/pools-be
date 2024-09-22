from django.db import models
from django.utils.translation import gettext_lazy as _

__author__ = 'snake'


class EmailSent(models.Model):
    """
    Instance of an email that was sent.
    """
    sent_to = models.CharField(_('Sent to email'), max_length=256)
    template = models.CharField(_('Template'), max_length=256)
    content = models.TextField(_('Content'))
    timestamp = models.DateTimeField(_('Timestamp'), auto_now_add=True)
    subject = models.CharField(_('Subject'), max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = _('Email sent')
        verbose_name_plural = _('Emails sent')

    def __str__(self):
        return '%s: %s' % (self.sent_to, self.template)