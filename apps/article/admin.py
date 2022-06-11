from django.contrib import admin
from markdown import markdown

from article.models import TagsModel, ArticleModel, CommentModel


class TagsAdmin(admin.ModelAdmin):
    model = TagsModel
    list_display = ["SlugTags", "NameTags",]
    list_display_links = ['SlugTags', 'NameTags',]
    search_fields = ['NameTags',]
    prepopulated_fields = {'SlugTags': ('NameTags',)}

admin.site.register(TagsModel, TagsAdmin)


class ArticleAdmin(admin.ModelAdmin):
    model = ArticleModel
    prepopulated_fields = {'slugArticle' : ('titleArticle',)}
    list_display = ['titleArticle', 'dateCreateArticle', 'authorArticle']
    list_display_links = ['titleArticle', 'dateCreateArticle', 'authorArticle']
    list_filter = ['dateCreateArticle', 'tagsArticle']
    search_fields =  ['titleArticle', 'textArticle', 'authorArticle', 'tagsArticle']

    fieldsets = (
        (None, {
            'fields' : ('titleArticle', 'slugArticle', 'textArticle', 'authorArticle', 'tagsArticle', 'viewArticle')
        }),

    )


class CommentAdmin(admin.ModelAdmin):
    model = CommentModel

    list_display = ['DateCreateComment', 'AuthorComment', 'ArticleAttcahmentComment']
    list_display_links = ['DateCreateComment', 'AuthorComment', 'ArticleAttcahmentComment']
    list_filter = ['DateCreateComment']
    search_fields =  ['TextComment']

admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(CommentModel, CommentAdmin)
