# Generated by Django 5.1 on 2024-12-04 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_alter_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
