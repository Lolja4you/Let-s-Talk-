from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import format_lazy
from django.contrib.auth.models import UserManager, AbstractBaseUser, AbstractUser, AnonymousUser, PermissionsMixin, Group, GroupManager, Permission
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from time import time


from users.managers import CustomUserManagers

class CustomUsers(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=333, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    
    photoUser = models.ImageField(_("photo"), upload_to='image/userImage/%Y/%m/', default='image/user/index.jpg')
    aboutUser = models.CharField(_('about me'), max_length=512, blank=True, null=True)
    
    date_joined = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = CustomUserManagers()

    def __str__(self):
        return self.email


    

    



