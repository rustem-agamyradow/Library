# Generated by Django 5.1 on 2024-12-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_user_desciption'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
