from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, default=False)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=13, default=False)
    image = models.ImageField(null = True, blank = True)
    password = models.CharField(max_length=100)
    profession = models.CharField(max_length=100, default=False)
    state = models.CharField(max_length=100, default=False)
    dist = models.CharField(max_length=50, default = True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
