# Generated by Django 2.2.5 on 2022-03-05 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20220303_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='Address',
        ),
        migrations.AlterField(
            model_name='address',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
    ]