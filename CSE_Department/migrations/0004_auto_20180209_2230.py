# Generated by Django 2.0.2 on 2018-02-09 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_Department', '0003_auto_20180209_2009'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserCounts',
        ),
        migrations.RenameField(
            model_name='conferencesattended',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='conferencesorg',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='otherjournals',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='paidscopus',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='scijournals',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='seminarsattended',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='seminarsorg',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='trainingprogattended',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='unpaidscopus',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='workshopsattended',
            old_name='employeeID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='workshopsorg',
            old_name='employeeID',
            new_name='user',
        ),
    ]
