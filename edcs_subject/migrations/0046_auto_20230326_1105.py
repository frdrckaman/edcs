# Generated by Django 3.1.7 on 2023-03-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0045_auto_20230319_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='cough_get_worse_after',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True, verbose_name='Has the patient had a long-standing cough that gets worse (After)'),
        ),
        migrations.AlterField(
            model_name='followup',
            name='cough_get_worse_before',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True, verbose_name='Has the patient had a long-standing cough that gets worse (Before)'),
        ),
        migrations.AlterField(
            model_name='historicalfollowup',
            name='cough_get_worse_after',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True, verbose_name='Has the patient had a long-standing cough that gets worse (After)'),
        ),
        migrations.AlterField(
            model_name='historicalfollowup',
            name='cough_get_worse_before',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=6, null=True, verbose_name='Has the patient had a long-standing cough that gets worse (Before)'),
        ),
    ]