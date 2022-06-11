from django.urls import path, include


from article.views import (
    ArticleView,
    ArticleDetailView,
    CreateArticleView,
    edit_article,
    TagsDetailView,
    delete_article,
    baseArticle,
    lastComment,
    dislikeArticle,
    likeArticle,
    #delete_comment
    )


app_name = 'article'

urlpatterns = [

    path('', ArticleView.as_view(), name='base'),
    path('article/', baseArticle, name='baseArticle'),

    path('article/<int:id>', ArticleDetailView.as_view(), name='detail'),
    path('article/create/', CreateArticleView.as_view(), name='create'),
    path('article/edit_article/change/<int:id>', edit_article, name='change_art'),
    path('article/edit_article/delete/<int:delete_id>', delete_article, name='delete_art'),
    path('article/analystics/dislike_art/<int:dislike_id>', dislikeArticle, name='dislike_art'),
    path('article/analystics/like_art/<int:like_id>', likeArticle, name='like_art'),
    #path('article/edit_comment/delete/<slug:article_slug>/<int:id>', delete_comment, name='delete_comment'),

    #path('article/analystics/dislike_comment/<int:dislike_id>', name='dislike_comment'),
    #path('article/analystics/like_comment/<int:like_id>', name='like_comment'),
    #path('article/edit_comment/change/<int:change_id>', name='change_comment'),

    path('tags/<slug:tag_slug>', TagsDetailView, name='tag_det'),
    path('last_comment/', lastComment, name='lastcomment'),

]

