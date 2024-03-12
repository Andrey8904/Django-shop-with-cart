from django.db import models


class CustomUser(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=256)
    user_created = models.DateTimeField(auto_now_add=True)
    user_agree = models.IntegerField()
    last_login = models.DateTimeField(auto_now=True)
    user_banned = models.IntegerField(default=0)
    user_activated = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'

        # почитать про клас мета