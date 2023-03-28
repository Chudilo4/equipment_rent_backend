from django.core.validators import MinValueValidator, FileExtensionValidator
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.title


class Equipment(models.Model):
    photo = models.FileField(upload_to='equipment/photo',
                             validators=[FileExtensionValidator(['png', 'jpeg', 'svg', 'jpg'])],
                             blank=False, verbose_name='Фото оборудования')
    title = models.CharField(max_length=255, blank=False,
                             null=False, verbose_name='Название оборудования')
    description = models.CharField(null=False, blank=False,
                                   verbose_name='Описание', max_length=95)
    quantity = models.IntegerField(verbose_name='Кол-во',
                                   validators=[MinValueValidator(1)],
                                   default=1, blank=False, null=False)
    price = models.IntegerField(verbose_name='Цена за смену',
                                validators=[MinValueValidator(1)],
                                default=1, blank=False, null=False)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория',
                            related_name='equipments')
    created_time = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Время создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.title


class Feedback(models.Model):
    fio = models.CharField(max_length=255, blank=False, null=False,
                           verbose_name='ФИО')
    phone_number = models.CharField(max_length=23, verbose_name='Номер телефона',
                                    blank=False, null=False)
    email = models.EmailField()
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Время создания')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.fio
