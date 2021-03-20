# Generated by Django 3.1.7 on 2021-03-19 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt',
            name='company',
        ),
        migrations.AddField(
            model_name='receipt',
            name='seller',
            field=models.CharField(default='', max_length=120, verbose_name='seller name'),
            preserve_default=False,
        ),
    ]
