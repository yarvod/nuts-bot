# Generated by Django 4.0.4 on 2022-12-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_alter_order_is_refused_alter_order_is_success'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='weight',
            field=models.IntegerField(choices=[(90, '90 грамм'), (170, '170 грамм'), (500, '500 грамм')], default=90, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='productweightprice',
            name='weight',
            field=models.IntegerField(choices=[(90, '90 грамм'), (170, '170 грамм'), (500, '500 грамм')], default=90, verbose_name='Вес'),
        ),
    ]
