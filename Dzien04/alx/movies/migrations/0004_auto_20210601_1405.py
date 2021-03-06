# Generated by Django 3.2.3 on 2021-06-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Ocena'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Plakat'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.URLField(blank=True, null=True, verbose_name='Link do trailera'),
        ),
    ]
