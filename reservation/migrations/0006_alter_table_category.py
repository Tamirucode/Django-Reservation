# Generated by Django 3.2.20 on 2023-07-17 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_alter_table_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='category',
            field=models.CharField(choices=[('B', 'Table for 3 people'), ('B', 'Table for 4 people'), ('B', 'Table for 6 people'), ('B', 'Table for 5 people'), ('D', 'Table for 2 people'), ('D', 'Table for 4 people'), ('D', 'Table for 6 people')], max_length=3),
        ),
    ]
