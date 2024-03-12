from django.db import models


class ProductRating(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    rating_value = models.IntegerField()
    data_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'
        index_together = (('id', 'product_id'),)