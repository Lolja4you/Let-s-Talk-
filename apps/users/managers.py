from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import GroupManager
from django.utils.translation import ugettext_lazy
from django.utils.text import slugify

from time import time

def create_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return str(new_slug)


class CustomUserManagers(BaseUserManager):

    def model_create_user(self, email, username, password, **extra_fields):
        
        if not email:
            raise ValueError(ugettext_lazy('Заполните поле "email"'))
        if not username:
            raise ValueError(ugettext_lazy('Заполните поле "Имя пользователя"'))
        if not password:
            raise ValueError(ugettext_lazy('Заполните поле "password"'))

        email = self.normalize_email(email)

        user = self.model(email=email, username = username, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, username, password):
        return self.model_create_user(email=email, username=username, password=password)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(ugettext_lazy('Superuser must have is_superuser=True.'))
        return self.model_create_user(email=email, password=password, username=username, **extra_fields)
