# Generated by Django 5.0.3 on 2024-08-09 13:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_dailynumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailynumbers',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
