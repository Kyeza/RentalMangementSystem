from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils import timezone

from users.constants import APPLICATION_STATUS
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


class Application(models.Model):
    owner = models.ForeignKey(LandLord, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey('rentals.Property', on_delete=models.CASCADE, null=True)
    applicant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    date_applied = models.DateTimeField(default=timezone.now, editable=False, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True, editable=False, default=APPLICATION_STATUS[0][0])

    def get_absolute_url(self):
        return reverse('users:application_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Application to {self.owner} from {self.applicant}'
