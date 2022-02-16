# Generated by Django 3.1.7 on 2022-02-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0016_auto_20220216_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcoholtobaccouse',
            name='tobacco_product',
            field=models.CharField(choices=[('yes_cigarettes', 'Yes, Cigarettes'), ('yes_cigars', 'Yes, Cigars'), ('yes_shisha', 'Yes, Shisha'), ('yes_pipes', 'Yes, pipes'), ('none_of_above', 'None of the above'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='If currently/past smoker, which tobacco products do you/ did you smoke.'),
        ),
        migrations.AlterField(
            model_name='historicalalcoholtobaccouse',
            name='tobacco_product',
            field=models.CharField(choices=[('yes_cigarettes', 'Yes, Cigarettes'), ('yes_cigars', 'Yes, Cigars'), ('yes_shisha', 'Yes, Shisha'), ('yes_pipes', 'Yes, pipes'), ('none_of_above', 'None of the above'), ('N/A', 'Not applicable')], default='N/A', max_length=45, verbose_name='If currently/past smoker, which tobacco products do you/ did you smoke.'),
        ),
    ]
