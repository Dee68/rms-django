# Generated by Django 3.2.18 on 2023-02-17 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meals',
            options={'verbose_name': 'meals', 'verbose_name_plural': 'meals'},
        ),
    ]