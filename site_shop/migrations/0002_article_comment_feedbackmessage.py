# Generated by Django 5.1rc1 on 2024-08-10 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название статьи')),
                ('abstract', models.TextField(verbose_name='Аннотация')),
                ('full_text', models.TextField(verbose_name='Текст статьи')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор комментария')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст комментария')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор комментария')),
                ('text', models.TextField(max_length=3000, verbose_name='Текст комментария')),
                ('responsible', models.CharField(max_length=100, verbose_name='Ответственный специалист')),
                ('status', models.BooleanField(verbose_name='Обработано')),
            ],
        ),
    ]
