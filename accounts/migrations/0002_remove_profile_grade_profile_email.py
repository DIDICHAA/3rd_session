# Generated by Django 4.2 on 2023-05-14 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="grade",
        ),
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
