from django.core.validators import MinValueValidator
from django.db import models


class CategoryEquipment(models.Model):
    title = models.CharField(verbose_name='Название категории',
                             max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.title


class Equipment(models.Model):
    photo = models.ImageField(upload_to='equipment/photo',
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
    category = models.ForeignKey(CategoryEquipment, verbose_name='Категория',
                                 on_delete=models.CASCADE, default=None)
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
