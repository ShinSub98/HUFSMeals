# Generated by Django 4.2.7 on 2024-02-26 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_menu_menu_image_menu_restaurant_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='restaurant_image',
            new_name='menu_image',
        ),
    ]
