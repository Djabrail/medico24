# Generated by Django 3.0.5 on 2020-04-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0002_auto_20200421_1741'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='clinic',
            field=models.ManyToManyField(to='clinics.Clinic'),
        ),
    ]
