# Generated by Django 5.0.1 on 2024-02-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0002_alter_customuser_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_activated',
            field=models.BooleanField(default=False),
        ),
    ]
