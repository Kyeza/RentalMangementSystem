from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import User, Tenant, LandLord


class TenantRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # using decorator to ensure data consistence in case of error in form.
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=True)
        user.is_tenant = True
        user.save()
        Tenant.objects.create(user=user)
        return user


class LandlordRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=True)
        user.is_landlord = True
        user.save()
        LandLord.objects.create(user=user)
        return user
