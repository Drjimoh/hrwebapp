# Generated by Django 2.2.1 on 2019-05-11 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_title', models.CharField(max_length=500, verbose_name='campaignTitle')),
                ('amount_raised', models.CharField(max_length=100, verbose_name='amountRaised')),
                ('goal', models.CharField(max_length=100)),
                ('currency_type', models.CharField(max_length=100, verbose_name='currencyType')),
                ('end_date', models.CharField(max_length=100, verbose_name='endDate')),
                ('number_contributors', models.CharField(max_length=100, verbose_name='numberContributors')),
                ('story', models.TextField()),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
