# Generated by Django 2.2.5 on 2019-09-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='item_images/%Y/%m/%d/'),
        ),
    ]