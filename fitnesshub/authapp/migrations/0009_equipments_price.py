# Generated by Django 5.0.2 on 2024-03-24 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_service_ends_on_service_fee_service_starts_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipments',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
