# Generated by Django 2.2.1 on 2019-05-11 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='amount_raised',
            new_name='amountRaised',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='campaign_title',
            new_name='campaignTitle',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='currency_type',
            new_name='currencyType',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='end_date',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='number_contributors',
            new_name='numberContributors',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='url',
            field=models.TextField(max_length=200),
        ),
    ]
