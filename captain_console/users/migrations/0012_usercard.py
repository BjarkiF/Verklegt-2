# Generated by Django 2.2 on 2020-05-13 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0011_auto_20200513_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=16)),
                ('exp_month', models.IntegerField(max_length=2)),
                ('exp_year', models.IntegerField(max_length=2)),
                ('cvc', models.IntegerField(max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]