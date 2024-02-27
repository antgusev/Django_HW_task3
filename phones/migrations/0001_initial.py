# Generated by Django 5.0.2 on 2024-02-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.IntegerField(verbose_name='price')),
                ('image', models.URLField(verbose_name='image')),
                ('release_date', models.DateField(verbose_name='release_date')),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
