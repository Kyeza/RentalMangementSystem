# Generated by Django 2.2.1 on 2019-05-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_landlord',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_tenant',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]