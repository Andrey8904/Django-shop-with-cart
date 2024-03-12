from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.CharField(max_length=100, db_index=True, verbose_name='Ссылка', unique=True)
    image = models.ImageField(upload_to='product/', verbose_name='Изображение')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.IntegerField()
    category = models.IntegerField(blank=False)
    available = models.BooleanField(default=True, verbose_name='Доступность')
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = (('id', 'slug'),)
        


    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'product_slug': self.slug})
