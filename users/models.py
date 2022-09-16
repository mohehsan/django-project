from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .utils.generator import username_generator


# Create your models here.
from users.manager import UserManager


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profile', default='profile/default.jpg')

    # Setting field
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Setting Object Manager
    objects = UserManager()

    class Meta:
        abstract = False


    def save(self, *args, **kwargs) -> None:
        if self.name == '':
            self.name = username_generator(self.email)
            return super().save(*args, **kwargs)

