# Generated by Django 3.1.7 on 2022-05-27 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0028_auto_20220519_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcoholtobaccouse',
            name='age_start_smoking',
            field=models.IntegerField(blank=True, help_text='in years', null=True, verbose_name='If past/current smoker, at what age did you first start smoking?'),
        ),
        migrations.AlterField(
            model_name='historicalalcoholtobaccouse',
            name='age_start_smoking',
            field=models.IntegerField(blank=True, help_text='in years', null=True, verbose_name='If past/current smoker, at what age did you first start smoking?'),
        ),
    ]
