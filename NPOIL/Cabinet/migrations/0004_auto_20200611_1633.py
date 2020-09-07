# Generated by Django 3.0.7 on 2020-06-11 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cabinet', '0003_auto_20200610_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name': 'Персональная информация', 'verbose_name_plural': 'Персональная информация'},
        ),
        migrations.AlterModelOptions(
            name='requisition',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterField(
            model_name='requisition',
            name='status_bool',
            field=models.BooleanField(default=False, verbose_name='Выполнен?'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Тема обращения')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('status', models.BooleanField(default=False, verbose_name='Решена?')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
    ]