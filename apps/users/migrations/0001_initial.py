# Generated by Django 3.0 on 2021-10-24 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUsers',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=333, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('photoUser', models.ImageField(default='image/user/index.jpg', upload_to='image/userImage/%Y/%m/', verbose_name='photo')),
                ('aboutUser', models.CharField(blank=True, max_length=512, null=True, verbose_name='about me')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('uniqueNameCustomUsers', models.CharField(db_index=True, max_length=21, unique=True)),
                ('slugCustomUser', models.SlugField(blank=True, null=True, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(to='auth.Group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
