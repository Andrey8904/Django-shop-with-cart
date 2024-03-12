from django.db import models



class Favorites(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id


