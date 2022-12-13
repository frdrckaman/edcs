# Generated by Django 3.1.7 on 2022-09-15 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcs_subject', '0038_auto_20220913_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalhousekitchensurrounding',
            name='material_exterior_wall',
            field=models.CharField(choices=[('no_walls', 'No walls'), ('mud', 'Mud'), ('bricks', 'Bricks'), ('wood', 'Wood'), ('cement_concrete', 'Cement/concrete'), ('stone', 'Stone'), ('metal', 'Metal'), ('OTHER', 'Others')], max_length=15, verbose_name='What is the main material of the exterior walls of the dwelling?'),
        ),
        migrations.AlterField(
            model_name='historicalhousekitchensurrounding',
            name='material_exterior_wall_kitchen',
            field=models.CharField(choices=[('no_walls', 'No walls'), ('mud', 'Mud'), ('bricks', 'Bricks'), ('wood', 'Wood'), ('cement_concrete', 'Cement/concrete'), ('stone', 'Stone'), ('metal', 'Metal'), ('OTHER', 'Others')], max_length=125, verbose_name='What is the main material of the exterior walls of your kitchen?'),
        ),
        migrations.AlterField(
            model_name='historicalhousekitchensurrounding',
            name='material_interior_wall',
            field=models.CharField(choices=[('no_walls', 'No walls'), ('mud', 'Mud'), ('bricks', 'Bricks'), ('wood', 'Wood'), ('cement_concrete', 'Cement/concrete'), ('stone', 'Stone'), ('metal', 'Metal'), ('OTHER', 'Others')], max_length=125, verbose_name='What is the main material of the interior walls of the dwelling?'),
        ),
        migrations.AlterField(
            model_name='historicalhousekitchensurrounding',
            name='material_interior_wall_kitchen',
            field=models.CharField(choices=[('no_walls', 'No walls'), ('mud', 'Mud'), ('bricks', 'Bricks'), ('wood', 'Wood'), ('cement_concrete', 'Cement/concrete'), ('stone', 'Stone'), ('metal', 'Metal'), ('OTHER', 'Others')], max_length=125, verbose_name='What is the main material of the interior walls of your kitchen?'),
        ),
        migrations.AlterField(
            model_name='housekitchensurrounding',
            name='material_exterior_wall',
            field=models.CharField(choices=[('no_walls', 'No walls'), ('mud', 'Mud'), ('bricks', 'Bricks'), ('wood', 'Wood'), ('cement_concrete', 'Cement/concrete'), ('stone', 'Stone'), ('metal', 'Metal'), ('OTHER', 'Others')], max_length=15, verbose_name='What is the main material of the exterior walls of the dwelling?'),
        ),
        migrations.AlterField(
            model_name='housekitchensurrounding',
            name='material_exterior_wall_kitchen',
            field=models.CharField(choices=[('no_walls', 'No walls'), ('mud', 'Mud'), ('bricks', 'Bricks'), ('wood', 'Wood'), ('cement_concrete', 'Cement/concrete'), ('stone', 'Stone'), ('metal', 'Metal'), ('OTHER', 'Others')], max_length=125, verbose_name='What is the main material of the exterior walls of your kitchen?'),
        ),
        migrations.AlterField(
            model_name='housekitchensurrounding',
            name='material_interior_wall',
            field=models.CharField(choices=[('no_walls', 'No walls'), ('mud', 'Mud'), ('bricks', 'Bricks'), ('wood', 'Wood'), ('cement_concrete', 'Cement/concrete'), ('stone', 'Stone'), ('metal', 'Metal'), ('OTHER', 'Others')], max_length=125, verbose_name='What is the main material of the interior walls of the dwelling?'),
        ),
        migrations.AlterField(
            model_name='housekitchensurrounding',
            name='material_interior_wall_kitchen',
            field=models.CharField(choices=[('no_walls', 'No walls'), ('mud', 'Mud'), ('bricks', 'Bricks'), ('wood', 'Wood'), ('cement_concrete', 'Cement/concrete'), ('stone', 'Stone'), ('metal', 'Metal'), ('OTHER', 'Others')], max_length=125, verbose_name='What is the main material of the interior walls of your kitchen?'),
        ),
    ]