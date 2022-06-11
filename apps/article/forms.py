from django.core.exceptions import ValidationError

from django import forms
from article.models import CommentModel, ArticleModel, TagsModel

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = CommentModel
        fields = ('TextComment',)

class ArticleForm(forms.ModelForm):

    class Meta:
        model = ArticleModel
        fields = ('titleArticle', 'textArticle', 'tagsArticle', 'slugArticle')
    
        widget = {
            'titleArticle' : forms.TextInput(attrs={'class' : 'none'}),
            'textArticle' : forms.Textarea(attrs={'class' : 'none'}),
            'tagsArticle' : forms.SelectMultiple(attrs={'class' : 'none'}),
            'slugArticle' : forms.TextInput(attrs={'class' : 'none'}),
        }
    
    def clean_slug(self):
        new_slug = self.cleaned_data['slugArticle'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be  "create" ')

class TagsForm(forms.ModelForm):

    class Meta:
        model = TagsModel
        fields = ('NameTags', 'SlugTags')

    widget = {
        'NameTags' : forms.TextInput(attrs={'class' : 'none'}),
        'SlugTags' : forms.TextInput(attrs={'class' : 'none'}),
    }
    def clean_slug(self):
        new_slug = self.cleaned_data['SlugTags'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')


    def save(self):
        new_tag = TagsModel.objects.create(
            NameTags = self.cleaned_data['NameTags'],
            SlugTags = self.cleaned_data['SlugTags'],
        )

        return new_tag
