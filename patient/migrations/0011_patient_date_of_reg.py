# Generated by Django 3.0.2 on 2020-02-09 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_patient_p_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_of_reg',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
