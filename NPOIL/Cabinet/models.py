from django.db import models
from django.contrib.auth.models import User, Group
from Home.models import Fuel

class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    docs_client = models.FileField('Документы клиента', upload_to=f'client/docs/', blank=True)
    phone = models.CharField('Телефон', max_length=30, blank=True)
    juristical_address = models.TextField('Юр. адрес', blank=True)
    agent_company = models.CharField('Представитель какой компании', max_length=80, blank=True)
    status = models.BooleanField('Информация проверена?', default=False)

    class Meta:
        verbose_name = 'Персональная информация'
        verbose_name_plural = 'Персональная информация'

    def __str__(self):
        return self.user.username

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    status = models.CharField('Статус заказа', max_length=250, default='Заказ обрабатывается')
    status_bool = models.BooleanField('Выполнен?', default=False)
    status_getting = models.BooleanField('Привязан к сотруднику?', default=False)
    volume = models.IntegerField('Объем', default=0)
    address = models.TextField('Адрес доставки')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.client.username}-{self.fuel.name} ({str(self.date)[:16]})'

class Requisition(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата взятия', auto_now_add=True)
    status_bool = models.BooleanField('Выполнен?', default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.employee.username} ({str(self.date)[:16]})'

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField('Тема обращения', max_length=50)
    message = models.TextField('Сообщение')
    status = models.BooleanField('Решена?', default=False)
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'

    def __str__(self):
        return f'{self.subject} ({str(self.date)[:16]})'

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    text = models.TextField('Ответ')
    date = models.DateTimeField('Дата ответа', auto_now_add=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'{self.user} ({str(self.date)[:16]})'