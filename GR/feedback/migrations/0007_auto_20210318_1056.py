# Generated by Django 3.1.7 on 2021-03-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0006_auto_20210316_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]