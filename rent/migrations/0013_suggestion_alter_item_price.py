# Generated by Django 4.1 on 2024-01-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rent", "0012_alter_item_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Suggestion",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="建议编号"
                    ),
                ),
                (
                    "ip",
                    models.CharField(default="", max_length=50, verbose_name="操作ip"),
                ),
                ("date", models.DateTimeField(verbose_name="提出时间")),
                (
                    "type",
                    models.CharField(default="", max_length=30, verbose_name="建议类型"),
                ),
                (
                    "detail",
                    models.CharField(default="", max_length=500, verbose_name="建议"),
                ),
                ("finish", models.BooleanField(default=False, verbose_name="是否完成")),
            ],
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.IntegerField(default=0, verbose_name="价格"),
        ),
    ]
