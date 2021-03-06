# Generated by Django 3.0.2 on 2020-01-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('officer_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
                ('o_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('email', models.EmailField(max_length=254)),
                ('aadhaar', models.CharField(max_length=30)),
                ('degree', models.CharField(max_length=30)),
            ],
        ),
    ]
