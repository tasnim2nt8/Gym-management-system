# Generated by Django 5.0.3 on 2024-04-18 18:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0023_enquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='notify',
            name='read_by_trainer',
        ),
        migrations.RemoveField(
            model_name='notify',
            name='read_by_user',
        ),
        migrations.DeleteModel(
            name='NotifUserStatus',
        ),
        migrations.DeleteModel(
            name='Notify',
        ),
    ]