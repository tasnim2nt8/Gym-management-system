# Generated by Django 5.0.2 on 2024-03-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_alter_appointment_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]