from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from django.db import models
from time import time

from users import models as us_models


class Chat(models.Model):
    class Meta:
        db_table = 'Chat'

    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )

    type = models.CharField(verbose_name="type", max_length=1, choices=CHAT_TYPE_CHOICES, default=DIALOG)
    members = models.ManyToManyField(us_models.CustomUsers, verbose_name=_("user"))

class Chat_message(models.Model):
    class Meta:
        ordering = ['pub_date']
        db_table = 'Chat message'

    body_message = models.TextField(_(""))

    pub_date = models.DateTimeField(_(""), default=timezone.now)
    is_readed = models.BooleanField(_(""), default=False)

    chat_attachment = models.ForeignKey(Chat, verbose_name=_("chat"), on_delete=models.CASCADE)
    user_attachment = models.ForeignKey(us_models.CustomUsers, verbose_name=_("user"), on_delete=models.CASCADE)

    def __str__(self):
        return self.body_message