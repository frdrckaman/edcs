# Generated by Django 3.1.7 on 2022-05-06 09:47

from django.db import migrations
import edcs_model.models.fields.other_charfield


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0013_auto_20220506_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='contraceptiveusereproductivehistory',
            name='contraceptives_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
        migrations.AddField(
            model_name='historicalcontraceptiveusereproductivehistory',
            name='contraceptives_other',
            field=edcs_model.models.fields.other_charfield.OtherCharField(blank=True, max_length=35, null=True, verbose_name='If other, please specify ...'),
        ),
    ]
