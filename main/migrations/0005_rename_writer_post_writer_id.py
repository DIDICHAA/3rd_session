# Generated by Django 4.2 on 2023-05-15 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_post_writer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="writer",
            new_name="writer_id",
        ),
    ]
