from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        max_length=150,
        editable=False,
        unique=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
        unique=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
        unique=False,
    )
    is_host = models.BooleanField(
        default=False,
    )
    email = models.EmailField(
        default="",
        unique=False,
    )
    avatar = models.URLField(blank=True)
