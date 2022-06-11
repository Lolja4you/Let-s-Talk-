# Generated by Django 3.0 on 2021-10-24 18:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleArticle', models.CharField(max_length=256, verbose_name='title')),
                ('textArticle', models.TextField(verbose_name='Text')),
                ('dateArticle', models.DateTimeField(auto_now_add=True)),
                ('dateCreateArticle', models.DateTimeField(default=django.utils.timezone.now)),
                ('slugArticle', models.SlugField(blank=True, unique=True, verbose_name='Url')),
            ],
            options={
                'db_table': 'Article',
            },
        ),
        migrations.CreateModel(
            name='TagsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SlugTags', models.SlugField(unique=True, verbose_name='URL')),
                ('NameTags', models.CharField(max_length=250, verbose_name='Name tag')),
            ],
            options={
                'db_table': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TextComment', models.TextField(verbose_name='body comment')),
                ('DateComment', models.DateTimeField(auto_now_add=True)),
                ('DateCreateComment', models.DateTimeField(default=django.utils.timezone.now)),
                ('ArticleAttcahmentComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleModel')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
    ]