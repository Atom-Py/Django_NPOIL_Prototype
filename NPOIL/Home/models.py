from django.db import models

class Distributor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    props = models.TextField(blank=True)
    description = models.TextField(blank=True)
    documents = models.FileField(upload_to=f'distributor/docs/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Дистрибьютор'
        verbose_name_plural = 'Дистрибьюторы'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField('Тип топлива', max_length=100, unique=True)
    slug = models.SlugField('URL', max_length=150, unique=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to=f'category/images/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Типы топлива'

    def __str__(self):
        return self.name

class Fuel(models.Model):
    type = models.ForeignKey(Category, related_name='type_fuel', on_delete=models.CASCADE)
    distributor = models.ForeignKey(Distributor, related_name='distributor_fuel', on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=100)
    slug = models.SlugField('URL', max_length=150, unique=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, help_text='цена за единицу объема/массы', default=0)
    image = models.ImageField('Изображение', upload_to=f'fuel/images/', blank=True)
    density = models.FloatField('Плотность', default=0)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Топливо'
        verbose_name_plural = 'Список топлива'

    def __str__(self):
        return f'{self.name} ({self.distributor})'
