# Generated by Django 3.2 on 2022-08-24 08:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bycicle_info',
            fields=[
                ('position', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, '빈 자리'), (1, '거치중'), (2, '도난')], validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
                ('rack_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Brack',
            fields=[
                ('position', models.IntegerField(primary_key=True, serialize=False)),
                ('bycicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bycicle_info')),
            ],
        ),
    ]
