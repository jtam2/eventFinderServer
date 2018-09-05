# Generated by Django 2.1 on 2018-09-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20180904_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='events',
            unique_together={('title', 'time', 'date')},
        ),
    ]
