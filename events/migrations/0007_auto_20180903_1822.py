# Generated by Django 2.1 on 2018-09-04 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20180903_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]