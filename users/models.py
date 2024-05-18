from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True,verbose_name='Avatar')

    class Meta:
        db_table = 'users'

        def __str__(self):
            return self.username