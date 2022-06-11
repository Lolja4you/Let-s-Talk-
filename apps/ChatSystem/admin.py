from django.contrib import admin

from ChatSystem import models as Ch_sys

class ChatAdmin(admin.ModelAdmin):
    model = Ch_sys.Chat
    list_display = ["type", ]
    list_display_links = ['type',]

    fieldsets = (
        (None, {
            "fields": (
                'type', 'members',
            ),
        }),
    )
    


admin.site.register(Ch_sys.Chat, ChatAdmin)
admin.site.register(Ch_sys.Chat_message)