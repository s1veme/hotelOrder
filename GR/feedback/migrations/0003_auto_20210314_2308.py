# Generated by Django 3.1.7 on 2021-03-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_reviews_date_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='slug',
            field=models.SlugField(default=1, max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviews',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Имя'),
        ),
    ]