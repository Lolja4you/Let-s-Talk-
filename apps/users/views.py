import os
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from article.models import CommentModel, ArticleModel
from users.models import CustomUsers
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from analytics.decorators import get_client_ip
from analytics.models import IpUser

from ChatSystem import models as ch_sys_model
from ChatSystem import forms as ch_sys_form


class ProfileUserView(TemplateView):
    def get(self, request, ):
        userArticle = ArticleModel.objects.filter(authorArticle=request.user.id)[:3]
        userComment = CommentModel.objects.filter(AuthorComment=request.user.id)[:5]
        ProfUser = CustomUsers.objects.get(pk=request.user.id)
        
        #system summing_all_views_users
        views_total=[]
        for art in userArticle:
            views_total.append(art.viewArticle.all().count())
        
        like_total=[]
        for art in userArticle:
            like_total.append(art.likeArticle.all().count())
        dislike_total=[]
        for art in userArticle:
            dislike_total.append(art.dislikeArticle.all().count())

        control_sum_view = sum(views_total)
        control_sum_rate = control_sum_view*0.5 + sum(like_total) - sum(dislike_total)


        
        if request.method == 'POST':
            form = CustomUserChangeForm(request.POST)
            if form.is_valid():
                userChange = form.save
                userChange.save()
                return HttpResponseRedirect(request.path_info) # все хорошо, коммент сохранен 

        else:
            form = CustomUserChangeForm()

        context = {
            'rate': control_sum_rate,
            'form' : form,
            'view' : control_sum_view,
            'customUser' : ProfUser,
            'userArticle' : userArticle,
            'userComment' : userComment,
        }

        return render(request, 'users/profile_private.html', context=context)


class PubProfileUserView(TemplateView):
    def get(self, request, id):
        ProfUser = CustomUsers.objects.get(id=id)
        if request.user == ProfUser:
            return redirect('users:profile')
        else:

            userPubArticle = ArticleModel.objects.filter(authorArticle=CustomUsers.objects.get(id=id).id)[:3]
            userPubComment = CommentModel.objects.filter(AuthorComment=CustomUsers.objects.get(id=id).id)[:3]
            
            form = ch_sys_form.ChatFrom()

            #system summing_all_views_users
            views_total=[]
            for art in userPubArticle:
                views_total.append(art.viewArticle.all().count())

            control_sum = sum(views_total)

            context = {
                'view' : control_sum,
                'customUser' : ProfUser,
                'userArticle' : userPubArticle,
                'userComment' : userPubComment,
                'form' : form
            }
            return render(request, 'users/profile_public.html', context=context)

    def post(self, request, pub_name_slug):
        DIALOG = 'D'
        if request.method == 'POST':
            form = ch_sys_form.ChatFrom(request.POST)
            if form.is_valid():
                chat = form.save(commit=False)
                chat.type = DIALOG 
                chat.save()
                form.save_m2m()
        context = {'form': chat}

        return render(request, 'users/profile_public.html', context=context)

class AllArticleUserView(TemplateView):
    def get(self, request):
        allUserArticle = ArticleModel.objects.filter(authorArticle=request.user.id)

        context = {
            'allUserArticle' : allUserArticle,
        }

        return render(request, 'users/article.html', context=context)

class AllCommentUserView(TemplateView):
    def get(self, request):
        allUserComment = CommentModel.objects.filter(AuthorComment=request.user.id)

        context = {
            'allUserComment' : allUserComment,
        }

        return render(request, 'users/comment.html', context=context)


