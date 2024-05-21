# Generated by Django 5.0.4 on 2024-04-23 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('short_desc', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='quantity')),
            ],
        ),
    ]
