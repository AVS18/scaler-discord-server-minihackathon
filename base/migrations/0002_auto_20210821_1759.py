# Generated by Django 3.1.2 on 2021-08-21 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='role',
            field=models.CharField(choices=[('Star', 'Star'), ('SuperStar', 'SuperStar'), ('Admin', 'Admin'), ('Megastar', 'Megastar')], max_length=20),
        ),
    ]
