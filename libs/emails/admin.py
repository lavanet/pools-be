from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import EmailSent

EmailSent.view = _('View')


class EmailSentAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (
            'sent_to',
            'subject',
            'timestamp',
            'template',
            'content',
        )}),
    )

    list_display = ('view', 'subject', 'sent_to', 'template', 'timestamp')
    search_fields = ('sent_to', 'timestamp', 'template', )
    readonly_fields = 'sent_to', 'timestamp', 'template', 'content',
    ordering = ('-timestamp', )

    change_form_template = "admin/change_form_emailsent.html"


admin.site.register(EmailSent, EmailSentAdmin)
