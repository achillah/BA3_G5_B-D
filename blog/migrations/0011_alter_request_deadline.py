# Generated by Django 4.0.2 on 2022-11-08 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_request_deadline_alter_request_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='deadline',
            field=models.DateField(),
        ),
    ]
