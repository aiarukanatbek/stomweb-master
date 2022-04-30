# Generated by Django 4.0.3 on 2022-04-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_service_delete_service_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20)),
                ('service_nunber', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]