# Generated by Django 3.1.7 on 2021-03-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_auto_20210316_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
