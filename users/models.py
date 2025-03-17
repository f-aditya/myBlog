from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # Tambahkan atribut tambahan jika diperlukan di sini
    # Contoh: bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
