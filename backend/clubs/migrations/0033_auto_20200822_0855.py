# Generated by Django 3.1 on 2020-08-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clubs", "0032_auto_20200821_1340"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="report",
            options={
                "ordering": ["name"],
                "permissions": [("generate_reports", "Can generate reports")],
            },
        ),
        migrations.AddField(
            model_name="report",
            name="public",
            field=models.BooleanField(default=False),
        ),
    ]
