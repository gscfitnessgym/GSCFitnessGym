# Generated by Django 4.2 on 2024-10-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(default='Default Address', max_length=50),
        ),
    ]