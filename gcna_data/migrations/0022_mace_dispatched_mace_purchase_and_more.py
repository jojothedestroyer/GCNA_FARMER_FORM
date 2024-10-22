# Generated by Django 4.2.1 on 2024-05-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0021_rename_from_station_dispatch_of_dried_nutmeg_rec_station_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mace_Dispatched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATION', models.CharField(choices=[('', '--Select Location--'), ('G', 'Grenville'), ('H', 'Hermitage'), ('M', 'Marli'), ('U', 'Union'), ('GP', 'Gouyave')], max_length=50, null=True, verbose_name='Station')),
                ('DATE_CREATED', models.DateField(null=True, verbose_name='Date of Sampling')),
                ('BATCH_CODE', models.CharField(max_length=50, null=True, verbose_name='Place of Purchase ')),
                ('DATE_OF_PURCHASE', models.DateField(null=True, verbose_name='Date of Purchase')),
                ('PLACE_OF_PURCHASE', models.CharField(choices=[('', '--Select Location--'), ('G', 'Grenville'), ('H', 'Hermitage'), ('M', 'Marli'), ('U', 'Union'), ('GP', 'Gouyave')], max_length=50, null=True, verbose_name='Place of Purchase ')),
                ('TOTAL_NUM_OF_FARMERS', models.CharField(default=0, max_length=50, verbose_name='Total Numbers of Farmers')),
                ('TOTAL_LBS_NUTMEG_BOUGHT', models.CharField(default=0, max_length=50, null=True, verbose_name='Total lbs of nutmeg bought')),
                ('NUM_OF_BAGS', models.CharField(default=0, max_length=50, verbose_name='Number of Bags')),
                ('MACE_1', models.CharField(default=0, max_length=50, verbose_name='Number of Bags')),
                ('MACE_2', models.CharField(default=0, max_length=50, verbose_name='Number of Bags')),
                ('MACE_3', models.CharField(default=0, max_length=50, verbose_name='Number of Bags')),
            ],
        ),
        migrations.CreateModel(
            name='Mace_Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATION', models.CharField(choices=[('', '--Select Location--'), ('G', 'Grenville'), ('H', 'Hermitage'), ('M', 'Marli'), ('U', 'Union'), ('GP', 'Gouyave')], max_length=50, null=True, verbose_name='Station')),
                ('DATE_CREATED', models.DateField(null=True, verbose_name='Date of Sampling')),
                ('BATCH_CODE', models.CharField(max_length=50, null=True, verbose_name='Place of Purchase ')),
                ('DATE_OF_PURCHASE', models.DateField(null=True, verbose_name='Date of Purchase')),
                ('PLACE_OF_PURCHASE', models.CharField(choices=[('', '--Select Location--'), ('G', 'Grenville'), ('H', 'Hermitage'), ('M', 'Marli'), ('U', 'Union'), ('GP', 'Gouyave')], max_length=50, null=True, verbose_name='Place of Purchase ')),
                ('TOTAL_NUM_OF_FARMERS', models.CharField(default=0, max_length=50, verbose_name='Total Numbers of Farmers')),
                ('TOTAL_LBS_NUTMEG_BOUGHT', models.CharField(default=0, max_length=50, null=True, verbose_name='Total lbs of nutmeg bought')),
                ('NUM_OF_BAGS', models.CharField(default=0, max_length=50, verbose_name='Number of Bags')),
                ('MACE_1', models.CharField(default=0, max_length=50, verbose_name='Number of Bags')),
                ('MACE_2', models.CharField(default=0, max_length=50, verbose_name='Number of Bags')),
                ('MACE_3', models.CharField(default=0, max_length=50, verbose_name='Number of Bags')),
                ('Vehicle_number', models.CharField(blank=True, max_length=50, null=True)),
                ('Delivery_advice_num', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='dispatch_of_green_nutmeg_rec',
            old_name='Vehicle_number',
            new_name='WAREHOUSE_RECEIPT_NUMBER',
        ),
    ]