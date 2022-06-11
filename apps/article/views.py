from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.urls import reverse

from article.models import ArticleModel, CommentModel, TagsModel
from article.forms import CommentForm, ArticleForm
from analytics.models import IpUser
from analytics.decorators import get_client_ip
from users.models import CustomUsers


class ArticleView(View):
    def get(self, request):
        article = ArticleModel.objects.all().order_by('-dateCreateArticle')[:10]
        context = {
            'article' : article,
        }
        return render(request, 'article/articleIndex.html', context=context)


class CreateArticleView(View):
    def get(self, request):
        form = ArticleForm()
        return render(request, 'article/createArticle.html', context={'form': form},)

    def post(self, request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                new_article = form.save(commit=False)
                new_article.authorArticle = request.user
                new_article.save() 
                form.save_m2m()      
                return redirect(new_article)
        
        return render(request, 'article/createArticle.html', context={'form': new_article},)


class ArticleDetailView(View):
    def get(self, request, id):
        article = get_object_or_404(ArticleModel, id=id)
        ip = get_client_ip(request)
        comment = CommentModel.objects.filter(ArticleAttcahmentComment=article.pk).order_by('-DateCreateComment')[:5]
        comment_form = CommentForm()


        if IpUser.objects.filter(ip=ip).exists():
            article.viewArticle.add(IpUser.objects.get(ip=ip))
        else:
            IpUser.objects.create(ip=ip)
            article.viewArticle.add(IpUser.objects.get(ip=ip))
        view = article.viewArticle.all().count()

        return render(
            request,
            'article/articleDetail.html',
            context={
                'article': article,
                'comment': comment,
                'form': comment_form,
            })

    def post(self, request, id):
        if request.method == 'POST':
            coment_form = CommentForm(data=request.POST)
            if coment_form.is_valid():
                artform = coment_form.save(commit=False)
                artform.AuthorComment = request.user
                artform.ArticleAttcahmentComment = get_object_or_404(ArticleModel, id = id)
                artform.save()
                return HttpResponseRedirect(request.path_info)
        else:
            coment_form = CommentForm()

        context = {
            'form': coment_form,
        }
        return render(request, 'article/articleDetail.html', context=context)


def dislikeArticle(request, dislike_id):
    article = ArticleModel.objects.get(pk=dislike_id)
    article.dislikeArticle.add(CustomUsers.objects.get(id=request.user.id))
    return redirect(article)

def likeArticle(request, like_id):
    article = ArticleModel.objects.get(pk=like_id)
    article.likeArticle.add(CustomUsers.objects.get(id=request.user.id))
    return redirect(article)

def baseArticle(request):
    return redirect('article:base')

def lastComment(request):
    comment = CommentModel.objects.all().order_by('-DateCreateComment')[:10]
    return render(request,'article/allComment.html', context={'comment':comment})

def TagsDetailView(request, tag_slug):
    tag = get_object_or_404(TagsModel, SlugTags=tag_slug)
    articleRevers = ArticleModel.objects.filter(tagsArticle=tag.pk).order_by('-dateCreateArticle')

    return render(request, 'article/tagDetail.html', context={'tag': tag, 'rev': articleRevers,})

def delete_article(request, delete_id):
    article_delete = ArticleModel.objects.get(pk=delete_id)
    if article_delete.authorArticle == request.user:                                                       #проверка на автора
        article_delete.delete()
    else:
        return redirect('article:base')
    return redirect('article:base')

def edit_article(request, id):
    tag = TagsModel.objects.all()
    try:
        change_article = ArticleModel.objects.get(pk=id)
        if change_article.authorArticle == request.user:                                                    #проверка на автора
            if request.method == 'POST':
                change_article.titleArticle = request.POST.get('titleArticle')
                change_article.textArticle = request.POST.get('textArticle')
                for tags in ArticleModel.objects.filter(tagsArticle__NameTags=change_article.tagsArticle):
                    tags_article = TagsModel.objects.get(NameTags=change_article.tagsArticle)
                    tags.tagsArticle.update(tags_article.id)
                    tags.tagsArticle.filter(NameTags=change_article.tagsArticle).delete()
                change_article.save()
                return redirect(change_article)
            else:
                return render(request, 'article/changeArticle.html', context={"edit": change_article, 'tag' : tag})
        else:                                                                                               #проверка не пройдена
            return redirect("article:base")   
    except ArticleModel.DoesNotExist:
        return redirect('article:base')

'''def delete_comment(request, article_slug, id):
    article = get_object_or_404(ArticleModel, slugArticle = article_slug)
    comment = CommentModel.objects.filter(ArticleAttcahmentComment=article.pk)
    comment_get = comment.objects.get(pk=id)
    if comment_delete_get.AuthorComment == request.user:
        comment_delete_get.delete()
    else:
        return redirect('article:base')
    return redirect('article:base')'''