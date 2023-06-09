# Generated by Django 4.1.3 on 2023-03-27 15:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField(default=True, verbose_name='This is a boolean field')),
                ('char', models.CharField(help_text='add help text', max_length=100, verbose_name='Name')),
                ('positive_int', models.PositiveIntegerField()),
                ('slug', models.SlugField(blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
    ]
