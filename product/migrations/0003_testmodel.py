# Generated by Django 3.2 on 2021-05-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_1', models.CharField(default='field_1', max_length=100)),
                ('field_2', models.CharField(default='field_2', max_length=100)),
            ],
        ),
    ]
