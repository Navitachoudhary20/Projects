# Generated by Django 4.2 on 2023-05-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acctholders', '0002_alter_acctholders_aadhaar_alter_acctholders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acctholders',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
