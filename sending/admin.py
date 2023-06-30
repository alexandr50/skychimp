from django.contrib import admin

from sending.models import Message, Sending, TrySending

admin.site.register(Message)
@admin.register(Sending)
class SendingAdmin(admin.ModelAdmin):

    list_display = ('user', 'get_customer', 'message', 'created_at', 'updated_at', 'interval', 'status_sending', 'start_sending', 'end_sending')
    readonly_fields = ('user', 'created_at', 'updated_at')

admin.site.register(TrySending)
