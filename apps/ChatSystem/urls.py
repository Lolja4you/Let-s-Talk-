from django.urls import path 

from ChatSystem import views as ch_sys_view


app_name = 'ch_sys'

urlpatterns = [
    path('talks_with_partner/', ch_sys_view.chatList.as_view(), name='ch'),
    path('talks_with_partner/<int:id>', ch_sys_view.messageList.as_view(), name='di'),
]
