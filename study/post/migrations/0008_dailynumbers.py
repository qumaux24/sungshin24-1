# Generated by Django 5.0.3 on 2024-08-09 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('daily1', models.IntegerField()),
                ('daily2', models.IntegerField()),
                ('daily3', models.IntegerField()),
            ],
        ),
    ]
