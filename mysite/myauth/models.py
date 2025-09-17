from django.db import models
from django.contrib.auth.models import User


def user_avatar_directory_path(instance: "Profile", filename: str) -> str:
    return "accounts/images/user_{pk}/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    agreement_accepted = models.BooleanField(default=True)
    avatar = models.ImageField(null=True, blank=True, upload_to=user_avatar_directory_path)
