from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.urls import reverse

from ChatSystem import models as ch_sys_model
from ChatSystem import forms as ch_sys_form

class chatList(View):
    def get(self, request):
        chat_list = ch_sys_model.Chat.objects.filter(members = request.user)
        form = ch_sys_form.ChatFrom()

        context = {'chat': chat_list, 'form' : form}
        return render(request, 'chat_system/main_chat_system.html', context=context)

    def post(self, request):
        if request.method == 'POST':
            form = ch_sys_form.ChatFrom(request.POST)
            if form.is_valid():
                new_chat = form.save(commit=False)
                new_chat.save()
                form.save_m2m()
                return redirect(request.path_info)
        context = {'form': new_chat}

        return render(request, 'chat_system/main_chat_system.html', context=context)

class messageList(View):
    def get(self, request, id):
        chat = ch_sys_model.Chat.objects.get(pk=id)
        message_list = ch_sys_model.Chat_message.objects.filter(chat_attachment = chat.id)
        
        message_form = ch_sys_form.MessageForm()

        context = {'list' : message_list, 'form' : message_form}

        return render(request, 'chat_system/private_dialog.html', context=context)
    
    def post(self, request, id):
        if request.method == 'POST':
            message_form = ch_sys_form.MessageForm(data=request.POST)
            if message_form.is_valid():
                mF = message_form.save(commit=False)
                mF.chat_attachment = get_object_or_404(ch_sys_model.Chat, pk = id)
                mF.user_attachment = request.user
                mF.save()
                return redirect(request.path_info)
            else:
                message_form = ch_sys_form.MessageForm()

            context = {'from' : message_form,}

        return render(request, 'chat_system/private_dialog.html', context=context)

