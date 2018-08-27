# Generated by Django 2.1 on 2018-08-27 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=200, null=True, unique=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Events')),
            ],
        ),
    ]