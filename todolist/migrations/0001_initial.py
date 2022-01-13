# Generated by Django 3.2.7 on 2022-01-12 06:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('catagory', models.CharField(choices=[('A', 'Assignment'), ('C', 'Chore'), ('G', 'Goal'), ('C', 'Self Care'), ('W', 'Work'), ('P', 'People')], max_length=1)),
                ('startdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('enddate', models.DateTimeField(blank=True)),
                ('remainingtime', models.DurationField(blank=True)),
                ('due', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
                ('repeated', models.CharField(choices=[('N', 'Never'), ('H', 'Hourly'), ('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], max_length=1)),
            ],
        ),
    ]