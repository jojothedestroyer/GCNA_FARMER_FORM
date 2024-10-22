# Generated by Django 4.2.1 on 2024-06-16 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0028_land_tenur_no_legal_title_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='Est_Production_Celery',
            field=models.CharField(max_length=50, null=True, verbose_name='What is the state of the celery Est_Production'),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='Est_Production_Hot_Pepper',
            field=models.CharField(max_length=50, null=True, verbose_name='What is the state of the hot pepper Est_Production'),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='Est_Production_Parsley',
            field=models.CharField(max_length=50, null=True, verbose_name='What is the state of the parsley Est_Production'),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='Est_Production_Petit_Bum',
            field=models.CharField(max_length=50, null=True, verbose_name='What is the state of the pwtit bum Est_Production'),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='Est_Production_Seasoning_Pepper',
            field=models.CharField(max_length=50, null=True, verbose_name='What is the state of the seasoning pepper Est_Production'),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='Est_Production_Thyme',
            field=models.CharField(max_length=50, null=True, verbose_name='What is the state of the THYME Est_Production'),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='Est_Production_chive',
            field=models.CharField(max_length=50, null=True, verbose_name='What is the state of the chive Est_Production'),
        ),
    ]