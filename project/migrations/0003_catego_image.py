# Generated by Django 5.1 on 2024-12-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_catego_category_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='catego',
            name='image',
            field=models.ImageField(default='prject/1.jpg', upload_to='project/%Y/%m/%d/'),
        ),
    ]
