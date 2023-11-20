import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


def uuid_default() -> uuid.UUID:
    return uuid.uuid4()


class User(AbstractUser):
    """
    Custom User Model.
    It is not really used right now but since it is best practice to use one we have it.
    """

    id = models.UUIDField(primary_key=True, default=uuid_default)
