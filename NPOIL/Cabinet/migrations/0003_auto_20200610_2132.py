# Generated by Django 3.0.7 on 2020-06-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cabinet', '0002_auto_20200610_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Заказ обрабатывается', max_length=250, verbose_name='Статус заказа'),
        ),
    ]
