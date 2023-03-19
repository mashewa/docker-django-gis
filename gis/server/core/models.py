"""Database models."""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager Methods for the Model User."""

    def create_user(
        self, email, first_name, last_name, phone, password=None, **extra_field
    ):
        if not email:
            raise ValueError("Email address required.")
        if not first_name:
            raise ValueError("First name required.")
        if not last_name:
            raise ValueError("Last name required.")
        if not phone:
            raise ValueError("Valid phone number required.")
        user = self.model(
            email=email.lower(),
            first_name=first_name.capitalize(),
            last_name=last_name.capitalize(),
            **extra_field,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=email.lower(),
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()
