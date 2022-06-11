
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.db.models import Sum
from markdown import markdown
from transliterate import translit, get_available_language_codes
from time import time

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from users.models import CustomUsers
from analytics.models import IpUser



def create_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return str(translit(new_slug, language_code='ru', reversed=True)) + '-' + str(int(time())) 


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def like(self):
        return self.get_queryset().filter(vote__gt=0)
    
    def dislike(self):
        return self.get_queryset().filter(vote__lt=0)
    
    def sum_rating(self):
        return self.get_queryset().aggregate(Sum("vote")).get('vote__sum') or 0

class TagsModel(models.Model):
    class Meta: 
        db_table = 'Tags'
    
    SlugTags = models.SlugField(verbose_name='URL', unique=True, db_index=True)
    NameTags = models.CharField(verbose_name='Name tag', max_length=250)

    def save(self, *args, **kwargs):
        self.SlugTags = slugify(self.NameTags)
        super(TagsModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.NameTags

    def get_absolute_url(self):
        return reverse(
            "article:tag_det",
            kwargs={
                "tag_slug": self.SlugTags,
            }
        )


class ArticleModel(models.Model):

    class Meta:
        db_table = 'Article'

    titleArticle = models.CharField(verbose_name='title', max_length=256)
    textArticle = models.TextField(verbose_name='Text')

    dateArticle = models.DateTimeField(auto_now_add=True)
    dateCreateArticle = models.DateTimeField(default=timezone.now)
    
    authorArticle = models.ForeignKey(CustomUsers, verbose_name=("Author"), on_delete=models.CASCADE, )
    tagsArticle = models.ManyToManyField(TagsModel, verbose_name=("Tag's"))

    viewArticle = models.ManyToManyField(IpUser, related_name='viewArticle', blank=True)

    slugArticle = models.SlugField(
        verbose_name='Url',unique=True,
        db_index=True, blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slugArticle = create_slug(self.titleArticle)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titleArticle

    def get_absolute_url(self):
        return reverse(
            "article:detail",
            kwargs={
                "id": self.id,
            }
        )


class CommentModel(models.Model):
    class Meta:
        db_table = 'Comment'

    TextComment = models.TextField(verbose_name='body comment')

    AuthorComment = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    ArticleAttcahmentComment = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)
    DateComment = models.DateTimeField(auto_now_add=True)
    DateCreateComment = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.DateCreateComment = timezone.now()
        self.save()

    def __str__(self):
        return self.TextComment




