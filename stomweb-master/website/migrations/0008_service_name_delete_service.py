# Generated by Django 4.0.3 on 2022-04-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_service_delete_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
