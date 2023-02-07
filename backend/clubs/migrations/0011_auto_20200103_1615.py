# Generated by Django 3.0.1 on 2020-01-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("clubs", "0010_note_notetag")]

    operations = [
        migrations.CreateModel(
            name="Major",
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
                ("name", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="School",
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
                ("name", models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name="profile",
            name="graduation_year",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="has_been_prompted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="club",
            name="target_majors",
            field=models.ManyToManyField(blank=True, to="clubs.Major"),
        ),
        migrations.AddField(
            model_name="club",
            name="target_schools",
            field=models.ManyToManyField(blank=True, to="clubs.School"),
        ),
        migrations.AddField(
            model_name="profile",
            name="major",
            field=models.ManyToManyField(blank=True, to="clubs.Major"),
        ),
        migrations.AddField(
            model_name="profile",
            name="school",
            field=models.ManyToManyField(blank=True, to="clubs.School"),
        ),
    ]