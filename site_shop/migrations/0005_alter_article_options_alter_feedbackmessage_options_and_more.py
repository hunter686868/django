# Generated by Django 5.0.7 on 2024-08-14 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("site_shop", "0004_alter_article_options_comment_article"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ["title"],
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
        migrations.AlterModelOptions(
            name="feedbackmessage",
            options={
                "verbose_name": "Сообщения поддержке",
                "verbose_name_plural": "Сообщения поддержке",
            },
        ),
        migrations.AlterModelOptions(
            name="section",
            options={
                "ordering": ("id",),
                "verbose_name": "Раздел",
                "verbose_name_plural": "Разделы",
            },
        ),
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.CharField(
                max_length=100, null=True, verbose_name="Автор комментария"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "Новый заказ"),
                    ("APR", "Подтвержден"),
                    ("PAY", "Оплачен"),
                    ("CNL", "Отменен"),
                ],
                default="NEW",
                max_length=3,
                verbose_name="Статус заказа",
            ),
        ),
        migrations.AlterField(
            model_name="orderline",
            name="count",
            field=models.IntegerField(
                default=1,
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Количество",
            ),
        ),
    ]