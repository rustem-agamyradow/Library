# Generated by Django 5.1 on 2024-12-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_bot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('desciption', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='prject/1.jpg', upload_to='project/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
