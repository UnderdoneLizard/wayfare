# Generated by Django 3.1.2 on 2020-10-08 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201007_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='temp', max_length=50),
            preserve_default=False,
        ),
    ]