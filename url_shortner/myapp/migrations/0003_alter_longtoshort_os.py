# Generated by Django 4.0.3 on 2022-04-07 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_longtoshort_os'),
    ]

    operations = [
        migrations.AlterField(
            model_name='longtoshort',
            name='os',
            field=models.CharField(max_length=50),
        ),
    ]