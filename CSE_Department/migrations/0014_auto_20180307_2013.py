# Generated by Django 2.0.2 on 2018-03-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE_Department', '0013_auto_20180307_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conferencesattended',
            name='orgInstitute',
            field=models.CharField(max_length=50, verbose_name='Organising Institute'),
        ),
        migrations.AlterField(
            model_name='conferencesattended',
            name='paperTitle',
            field=models.CharField(max_length=50, verbose_name='Paper Title'),
        ),
        migrations.AlterField(
            model_name='conferencesorg',
            name='fundingAgency',
            field=models.CharField(max_length=100, verbose_name='Funding Agency'),
        ),
        migrations.AlterField(
            model_name='conferencesorg',
            name='orgInstitute',
            field=models.CharField(max_length=50, verbose_name='Organising Institute'),
        ),
        migrations.AlterField(
            model_name='otherjournals',
            name='corresAuthors',
            field=models.CharField(max_length=100, verbose_name='Corresponding Authors'),
        ),
        migrations.AlterField(
            model_name='otherjournals',
            name='impactFac',
            field=models.CharField(max_length=50, verbose_name='Impact Factor'),
        ),
        migrations.AlterField(
            model_name='otherjournals',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='otherjournals',
            name='paperTitle',
            field=models.CharField(max_length=50, verbose_name='Paper Title'),
        ),
        migrations.AlterField(
            model_name='otherjournals',
            name='pp',
            field=models.CharField(max_length=50, verbose_name='PP'),
        ),
        migrations.AlterField(
            model_name='paidscopus',
            name='corresAuthors',
            field=models.CharField(max_length=100, verbose_name='Corresponding Authors'),
        ),
        migrations.AlterField(
            model_name='paidscopus',
            name='impactFac',
            field=models.CharField(max_length=50, verbose_name='Impact Factor'),
        ),
        migrations.AlterField(
            model_name='paidscopus',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='paidscopus',
            name='paperTitle',
            field=models.CharField(max_length=50, verbose_name='Paper Title'),
        ),
        migrations.AlterField(
            model_name='paidscopus',
            name='pp',
            field=models.CharField(max_length=50, verbose_name='PP'),
        ),
        migrations.AlterField(
            model_name='scijournals',
            name='impactFac',
            field=models.CharField(max_length=50, verbose_name='Impact Factor'),
        ),
        migrations.AlterField(
            model_name='scijournals',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='scijournals',
            name='pp',
            field=models.CharField(max_length=50, verbose_name='PP'),
        ),
        migrations.AlterField(
            model_name='seminarsattended',
            name='orgInstitute',
            field=models.CharField(max_length=50, verbose_name='Organising Institute'),
        ),
        migrations.AlterField(
            model_name='seminarsattended',
            name='paperTitle',
            field=models.CharField(max_length=50, verbose_name='Paper Title'),
        ),
        migrations.AlterField(
            model_name='seminarsorg',
            name='fundingAgency',
            field=models.CharField(max_length=100, verbose_name='Funding Agency'),
        ),
        migrations.AlterField(
            model_name='seminarsorg',
            name='orgInstitute',
            field=models.CharField(max_length=50, verbose_name='Organising Institute'),
        ),
        migrations.AlterField(
            model_name='trainingprogattended',
            name='orgInstitute',
            field=models.CharField(max_length=50, verbose_name='Organising Institute'),
        ),
        migrations.AlterField(
            model_name='unpaidscopus',
            name='corresAuthors',
            field=models.CharField(max_length=100, verbose_name='Corresponding Authors'),
        ),
        migrations.AlterField(
            model_name='unpaidscopus',
            name='impactFac',
            field=models.CharField(max_length=50, verbose_name='Impact Factor'),
        ),
        migrations.AlterField(
            model_name='unpaidscopus',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='unpaidscopus',
            name='paperTitle',
            field=models.CharField(max_length=50, verbose_name='Paper Title'),
        ),
        migrations.AlterField(
            model_name='unpaidscopus',
            name='pp',
            field=models.CharField(max_length=50, verbose_name='PP'),
        ),
        migrations.AlterField(
            model_name='workshopsattended',
            name='orgInstitute',
            field=models.CharField(max_length=50, verbose_name='Organising Institute'),
        ),
        migrations.AlterField(
            model_name='workshopsorg',
            name='fundingAgency',
            field=models.CharField(max_length=100, verbose_name='Funding Agency'),
        ),
        migrations.AlterField(
            model_name='workshopsorg',
            name='orgInstitute',
            field=models.CharField(max_length=50, verbose_name='Organising Institute'),
        ),
    ]
