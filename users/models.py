from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .utils import get_image_filename


class User(AbstractUser):
    is_tenant = models.BooleanField(null=True, blank=True, default=False)
    is_landlord = models.BooleanField(null=True, blank=True, default=False)


class Tenant(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(null=True, blank=True, default='default.png', upload_to=get_image_filename)
    phone_number = models.CharField(max_length=50, null=True, blank=True,
                                    validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                               message='Enter a valid phone number.')])

    def __str__(self):
        return f'{self.user}'


class LandLord(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(null=True, blank=True, default='default.png', upload_to=get_image_filename)
    phone_number = models.CharField(max_length=50, null=True, blank=True,
                                    validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                                               message='Enter a valid phone number.')])

    def __str__(self):
        return f'{self.user}'
