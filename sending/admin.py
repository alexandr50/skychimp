from django.contrib import admin

from sending.models import Message, Sending, TrySending

admin.site.register(Message)
admin.site.register(Sending)
admin.site.register(TrySending)
