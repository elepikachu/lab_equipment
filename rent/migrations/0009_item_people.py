# Generated by Django 4.1 on 2024-01-03 01:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rent", "0008_alter_item_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="people",
            field=models.CharField(default="", max_length=20, verbose_name="负责人"),
        ),
    ]