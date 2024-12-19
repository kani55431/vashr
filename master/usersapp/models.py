from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    department = models.CharField(
        max_length=20,
        choices=[
            ('masteruser', 'Master User'),
            ('hruser', 'HR User'),
        ],
        default='admin'
    )

    def has_role(self, role):
        return self.department == role
