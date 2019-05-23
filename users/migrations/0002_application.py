# Generated by Django 2.2.1 on 2019-05-23 20:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_property_owner'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_applied', models.DateTimeField(blank=True, default=django.utils.timezone.now, editable=False)),
                ('status', models.CharField(blank=True, default='PENDING', editable=False, max_length=15, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Tenant')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.LandLord')),
                ('property', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rentals.Property')),
            ],
        ),
    ]
