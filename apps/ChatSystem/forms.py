from django.core.exceptions import ValidationError
from django import forms

from ChatSystem import models as ch_sys

class MessageForm(forms.ModelForm):
    class Meta:
        model = ch_sys.Chat_message
        fields = ('body_message',)

class ChatFrom(forms.ModelForm):
    class Meta:
        model = ch_sys.Chat
        exlude = ()
        fields = ('type', 'members',)

        widget = {
            'type' : forms.TextInput(attrs={'class' : 'none'}),
            'members' : forms.SelectMultiple(attrs={'class' : 'none'}),
        }

