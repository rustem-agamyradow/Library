# Generated by Django 5.1 on 2024-12-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(null=True, upload_to='file/'),
        ),
    ]