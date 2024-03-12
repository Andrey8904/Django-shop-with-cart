from django.db import models


class AddReview(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    text_review = models.TextField(max_length=1000)
    data_review = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('user_id', )
        verbose_name = 'Reviews'
        verbose_name_plural = 'Reviews'
