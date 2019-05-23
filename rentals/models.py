from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    owner = models.ForeignKey('users.LandLord', on_delete=models.CASCADE, editable=False)
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(default='img_default.png', upload_to='property_imgs')
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    date_listed = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('rentals:property_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
