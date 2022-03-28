# Generated by Django 3.1.7 on 2022-02-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicalreview',
            name='use_dm_medication',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('decline_to_answer', 'Decline to answer'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='Are you using any medications?'),
        ),
        migrations.AlterField(
            model_name='historicalclinicalreview',
            name='use_dm_medication',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('decline_to_answer', 'Decline to answer'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='Are you using any medications?'),
        ),
    ]