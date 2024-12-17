# Generated by Django 5.1 on 2024-12-03 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_catego_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='available',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date',
        ),
        migrations.RemoveField(
            model_name='category',
            name='desciption',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name:')),
                ('desciption', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='prject/1.jpg', upload_to='project/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Catego',
        ),
    ]
