from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Section(models.Model):
    title = models.CharField(
        max_length=100,
        help_text='Введите название раздела',
        unique=True,
        verbose_name='Название раздела'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    section = models.ForeignKey('Section', on_delete=models.SET_NULL, null=True, verbose_name='Раздел')
    title = models.CharField(max_length=70, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title


class Discount(models.Model):
    code = models.CharField(max_length=10, verbose_name='Код купона')
    value = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        verbose_name='Размер скидки',
        help_text='В процентах'
    )

    class Meta:
        ordering = ['-value']
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.code} ({str(self.value)})'


class Order(models.Model):
    need_delivery = models.BooleanField(verbose_name='Необходима доставка')
    discount = models.ForeignKey(Discount, verbose_name='Скидка', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=70, verbose_name='Имя')
    phone = models.CharField(max_length=70, verbose_name='Телефон')
    email = models.EmailField()
    address = models.TextField(verbose_name='Адрес', blank=True)
    notice = models.CharField(max_length=150, verbose_name='Примечание к заказу', blank=True)
    date_order = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    date_send = models.DateTimeField(null=True, blank=True, verbose_name='Дата отправки')

    STATUSES = [
        ('NEW', 'Новый заказ'),
        ('APR', 'Подтвержден'),
        ('PAY', 'Оплачен'),
        ('CNL', 'Отменен')
    ]

    status = models.CharField(choices=STATUSES, max_length=3, default='NEW', verbose_name='Статус заказа')

    class Meta:
        ordering = ['-date_order']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'ID {self.id}'


class OrderLine(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0)
    count = models.IntegerField(verbose_name='Количество', validators=[MinValueValidator(1)], default=1)

    class Meta:
        verbose_name = 'Строка заказа'
        verbose_name_plural = 'Строки заказов'

    def __str__(self):
        return f'Заказ ({self.order.id}) {self.product.title}: {self.count}'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статьи')
    author = models.CharField(max_length=100, verbose_name='Автор комментария', null=True)
    date = models.DateField(verbose_name='Дата написания', null=True)
    abstract = models.TextField(verbose_name='Аннотация')
    full_text = models.TextField(verbose_name='Текст статьи')

    class Meta:
        ordering = ['title']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name='Статья', on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=100, verbose_name='Автор комментария')
    text = models.TextField(max_length=3000, verbose_name='Текст комментария')

    def __str__(self):
        return f'Комментарий от {self.author} к статье {self.article}'


class FeedbackMessage(models.Model):
    author = models.CharField(max_length=100, verbose_name='Автор комментария')
    text = models.TextField(max_length=3000, verbose_name='Текст комментария')
    responsible = models.CharField(max_length=100, verbose_name='Ответственный специалист')
    status = models.BooleanField(verbose_name='Обработано')

    class Meta:
        verbose_name = 'Сообщения поддержке'
        verbose_name_plural = 'Сообщения поддержке'

