# Generated by Django 3.1.1 on 2020-09-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patoa', '0002_auto_20200917_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claimset',
            name='add112',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='claimset',
            name='claim_list',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='claimset',
            name='obj',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]