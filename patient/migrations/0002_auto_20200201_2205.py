# Generated by Django 3.0.2 on 2020-02-01 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='spouse',
            new_name='relation',
        ),
    ]