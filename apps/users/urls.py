from django.urls import path 
from django.contrib.auth.decorators import login_required

from users.views import (
    ProfileUserView,
    PubProfileUserView,
    AllCommentUserView,
    AllArticleUserView,
    )

app_name = 'users'

urlpatterns = [
    path('account/profile/', login_required(ProfileUserView.as_view()), name='profile'),
    path('account/profile/all_article_user', login_required(AllArticleUserView.as_view()), name="all_article"),
    path('account/profile/all_comment_user', login_required(AllCommentUserView.as_view()), name="all_comment"),
    path('accounts/profile/<int:id>', PubProfileUserView.as_view(), name="prof"),
]
