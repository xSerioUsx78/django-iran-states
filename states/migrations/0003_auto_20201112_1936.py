# Generated by Django 3.1.3 on 2020-11-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0002_cities_states'),
    ]

    operations = [
        migrations.AlterField(
            model_name='states',
            name='city',
            field=models.ManyToManyField(blank=True, to='states.Cities'),
        ),
    ]
