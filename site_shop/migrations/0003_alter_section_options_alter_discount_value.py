# Generated by Django 5.1rc1 on 2024-08-10 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_shop', '0002_article_comment_feedbackmessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('id',), 'verbose_name': ('Раздел',), 'verbose_name_plural': 'Разделы'},
        ),
        migrations.AlterField(
            model_name='discount',
            name='value',
            field=models.IntegerField(help_text='В процентах', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Размер скидки'),
        ),
    ]
