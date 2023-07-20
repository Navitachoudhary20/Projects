# Generated by Django 4.1.6 on 2023-04-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelling', '0003_user_delete_authentication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]