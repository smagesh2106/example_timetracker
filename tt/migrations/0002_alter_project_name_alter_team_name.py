# Generated by Django 4.2.2 on 2023-07-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
