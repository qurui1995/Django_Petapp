# Generated by Django 4.2.1 on 2023-06-06 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('F', 'Pet Food'), ('T', 'Toy'), ('S', 'Pet Service')], max_length=2),
        ),
    ]
