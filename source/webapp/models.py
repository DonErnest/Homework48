from django.db import models

category_choices = [('clothes', 'Одежда'),('jewelry', 'Украшения'),
                    ('kitchenware','Для кухни'),('hobby', 'Хобби'),
                    ('garden', 'Для сада')]


class Item(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(max_length = 12, verbose_name='Категория',
                              default= category_choices[0][0], choices=category_choices)
    amount = models.PositiveIntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена' )

    def __str__(self):
        return self.description
