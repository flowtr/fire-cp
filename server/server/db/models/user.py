from django.db.models import Model, CharField
from django.contrib.auth.models import AbstractBaseUser

# Django typed model for better accessibility
from typedmodels.models import TypedModel


class User(TypedModel, AbstractBaseUser):
    username = CharField(max_length=40, unique=True)
    email = CharField()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["username", "email", "password"]
