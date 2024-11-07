# Generated by Django 4.2 on 2024-11-07 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0017_membershipreport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membershipreport',
            old_name='total_active_members',
            new_name='active_members',
        ),
        migrations.RenameField(
            model_name='membershipreport',
            old_name='total_inactive_members',
            new_name='inactive_members',
        ),
        migrations.RenameField(
            model_name='membershipreport',
            old_name='total_active_pricing',
            new_name='total_pricing',
        ),
        migrations.RemoveField(
            model_name='membershipreport',
            name='report_date',
        ),
        migrations.RemoveField(
            model_name='membershipreport',
            name='total_inactive_pricing',
        ),
    ]