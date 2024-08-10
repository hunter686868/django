# Generated by Django 5.1rc1 on 2024-08-10 10:01

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Код купона')),
                ('value', models.ImageField(help_text='В процентах', upload_to='', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Размер скидки')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название раздела', max_length=100, unique=True, verbose_name='Название раздела')),
            ],
            options={
                'verbose_name': ('Раздел',),
                'verbose_name_plural': 'Разделы',
                'ordering': (['id'],),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_delivery', models.BooleanField(verbose_name='Необходима доставка')),
                ('name', models.CharField(max_length=70, verbose_name='Имя')),
                ('phone', models.CharField(max_length=70, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
                ('notice', models.CharField(blank=True, max_length=150, verbose_name='Примечание к заказу')),
                ('date_order', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('date_send', models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки')),
                ('status', models.CharField(choices=[('NEW', 'Новый заказ'), ('APR', 'Подтвержден'), ('PAY', 'Оплачен'), ('CNL', 'Отменен')], default=('NEW', 'Новый заказ'), max_length=3, verbose_name='Статус заказа')),
                ('discount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_shop.discount', verbose_name='Скидка')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-date_order'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='photos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='site_shop.album')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('count', models.ImageField(default=1, upload_to='', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_shop.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_shop.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Строка заказа',
                'verbose_name_plural': 'Строки заказов',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_shop.section', verbose_name='Раздел'),
        ),
    ]