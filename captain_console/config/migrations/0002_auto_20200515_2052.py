# Generated by Django 2.2 on 2020-05-15 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='lat',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='config',
            name='log',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='config',
            name='zoom',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]