# Generated by Django 2.2.5 on 2019-09-26 16:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("clubs", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="club",
            name="parent_orgs",
            field=models.ManyToManyField(to="clubs.Club"),
        ),
        migrations.CreateModel(
            name="Badge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("color", models.CharField(default="", max_length=16)),
                (
                    "org",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clubs.Club",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="club",
            name="badges",
            field=models.ManyToManyField(to="clubs.Badge"),
        ),
    ]