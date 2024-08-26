from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import UserManager as DefaultUserManager


class CustomUserManager(DefaultUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O campo email é obrigatório")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    session_token = models.CharField(max_length=100, blank=True, null=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.username
