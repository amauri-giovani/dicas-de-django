# Generated by Django 3.2.6 on 2021-08-16 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=200, verbose_name='destino')),
                ('date_travel', models.DateField(blank=True, null=True, verbose_name='data')),
                ('datetime_travel', models.DateTimeField(blank=True, null=True, verbose_name='data/hora')),
                ('time_travel', models.TimeField(blank=True, null=True, verbose_name='tempo')),
                ('duration_travel', models.DurationField(blank=True, null=True, verbose_name='duração')),
            ],
            options={
                'verbose_name': 'viagem',
                'verbose_name_plural': 'viagens',
                'ordering': ('destination',),
            },
        ),
    ]
