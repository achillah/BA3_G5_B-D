# Generated by Django 4.1.2 on 2022-10-17 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('reference_number', models.IntegerField()),
                ('start_date', models.DateField()),
                ('deadline', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('priority', models.CharField(choices=[('1', 'Highest'), ('2', 'High'), ('3', 'Medium'), ('4', 'Low'), ('5', 'Lowest')], default='3', max_length=10)),
                ('faction', models.CharField(max_length=100)),
                ('consultant', models.CharField(max_length=100)),
                ('main_skills', models.CharField(max_length=100)),
                ('consultant_level', models.CharField(choices=[('1', 'Junior'), ('2', 'Senior')], default='1', max_length=10)),
                ('status', models.CharField(choices=[('1', 'Done'), ('2', 'Pending'), ('3', 'To be done')], default='3', max_length=10)),
                ('date_requested', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]