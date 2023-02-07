# Generated by Django 3.1.2 on 2020-10-25 18:28

from django.db import migrations


def update_application_enum(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Club = apps.get_model("clubs", "Club")
    for club in Club.objects.all():
        application_required = club.application_required
        if application_required == 1:
            club.application_required = 1
        elif application_required == 2 or application_required == 3:
            club.application_required = 4
        club.save()


class Migration(migrations.Migration):

    dependencies = [
        ("clubs", "0051_auto_20201025_1428"),
    ]

    operations = [migrations.RunPython(update_application_enum)]