# Generated by Django 5.0.6 on 2024-08-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
