"""Define custom user model """
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from main.models import Team


class MyUserManager(BaseUserManager):
    """Manager for MyUser model"""
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=self.normalize_email(username)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    """Custom user model that supports additional fields favorite_team."""
    username = models.CharField(max_length=40, unique=True)
    favorite_team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
