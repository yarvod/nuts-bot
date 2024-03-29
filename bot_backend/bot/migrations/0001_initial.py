# Generated by Django 4.0.4 on 2022-12-24 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Заказ активен')),
                ('is_refused', models.BooleanField(default=True, verbose_name='Заказ отменен')),
                ('is_success', models.BooleanField(default=True, verbose_name='Заказ успешно завершен')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('finished', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Есть в наличии')),
                ('slug', models.SlugField(help_text='Уникальная строка', verbose_name='Идентификатор')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='media/photos/products', verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductWeightPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(choices=[(90, '90 грамм'), (180, '180 грамм'), (500, '500 грамм')], default=90, verbose_name='Вес')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Развесовка продукта',
                'verbose_name_plural': 'Развесовки продукта',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество упаковок')),
                ('weight', models.IntegerField(choices=[(90, '90 грамм'), (180, '180 грамм'), (500, '500 грамм')], default=90, verbose_name='Вес')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='bot.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Продукт в заказе',
                'verbose_name_plural': 'Продукты в заказе',
            },
        ),
    ]
