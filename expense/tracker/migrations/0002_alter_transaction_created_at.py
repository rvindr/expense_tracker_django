# Generated by Django 4.2.14 on 2024-07-25 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
