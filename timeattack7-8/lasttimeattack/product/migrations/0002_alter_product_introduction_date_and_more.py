# Generated by Django 4.1 on 2022-08-12 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='introduction_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='purchase_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='subscription_enddate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='subscription_startdate',
            field=models.DateTimeField(),
        ),
    ]