# Generated by Django 2.2.5 on 2022-03-03 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(default='Wenzhe', max_length=32, verbose_name='name'),
        ),
    ]
