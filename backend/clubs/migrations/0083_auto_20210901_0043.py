# Generated by Django 3.2.6 on 2021-09-01 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clubs", "0082_clubfairbooth"),
    ]

    operations = [
        migrations.AddField(
            model_name="clubapplication",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="applicationquestion",
            name="question_type",
            field=models.IntegerField(
                choices=[
                    (1, "Free Response"),
                    (2, "Multiple Choice"),
                    (3, "Short Answer"),
                    (4, "Informational Text"),
                ],
                default=1,
            ),
        ),
    ]
