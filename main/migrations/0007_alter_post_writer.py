# Generated by Django 4.2 on 2023-05-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_rename_writer_id_post_writer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="writer",
            field=models.CharField(max_length=200),
        ),
    ]
