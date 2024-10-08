# Generated by Django 5.0.7 on 2024-08-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_customerrequest_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('service', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
