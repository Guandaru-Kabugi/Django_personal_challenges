# Generated by Django 5.0.6 on 2024-07-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://i.ytimg.com/vi/qnEjanlGXok/maxresdefault.jpg', max_length=500),
        ),
    ]
