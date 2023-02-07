# Generated by Django 3.2.6 on 2021-10-03 16:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("clubs", "0086_applicationsubmission_archived"),
    ]

    operations = [
        migrations.AddField(
            model_name="questionanswer",
            name="users_liked",
            field=models.ManyToManyField(
                related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]