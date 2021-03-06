# Generated by Django 2.2 on 2019-09-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('category', models.CharField(choices=[('clothes', 'Одежда'), ('jewelry', 'Украшения'), ('kitchenware', 'Для кухни'), ('hobby', 'Хобби'), ('garden', 'Для сада')], default='clothes', max_length=12, verbose_name='Категория')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
            ],
        ),
    ]
