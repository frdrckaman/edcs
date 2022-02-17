# Generated by Django 3.1.7 on 2022-02-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0030_auto_20220217_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidinfectionhistory',
            name='have_covid_symptoms',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='Did you have any symptoms when you first knew or thought you had COVID-19?'),
        ),
        migrations.AlterField(
            model_name='covidinfectionhistory',
            name='swab_test_results',
            field=models.CharField(choices=[('positive_test', 'One or more positive test(s) '), ('negative_test', 'One or more negative tests, but none were positive'), ('all_test_failed', 'All tests failed'), ('waiting_results', 'Waiting for all results'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='If yes, What was the result/were the results of all swab tests you’ve had?'),
        ),
        migrations.AlterField(
            model_name='historicalcovidinfectionhistory',
            name='have_covid_symptoms',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='Did you have any symptoms when you first knew or thought you had COVID-19?'),
        ),
        migrations.AlterField(
            model_name='historicalcovidinfectionhistory',
            name='swab_test_results',
            field=models.CharField(choices=[('positive_test', 'One or more positive test(s) '), ('negative_test', 'One or more negative tests, but none were positive'), ('all_test_failed', 'All tests failed'), ('waiting_results', 'Waiting for all results'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='If yes, What was the result/were the results of all swab tests you’ve had?'),
        ),
    ]
