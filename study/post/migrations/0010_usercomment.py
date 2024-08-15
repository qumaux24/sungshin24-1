# Generated by Django 5.0.7 on 2024-08-14 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_alter_dailynumbers_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usercomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usercomment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('userpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.userpost')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
