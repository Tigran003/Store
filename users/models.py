from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True,verbose_name='Avatar')
    phone_number = models.CharField(max_length=12, null=True, blank=True)

    class Meta:
        db_table = 'users'

        def __str__(self):
            return self.username