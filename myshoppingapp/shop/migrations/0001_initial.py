# Generated by Django 5.0.6 on 2024-07-02 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150)),
                ('item_descp', models.CharField(max_length=150)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
