# Generated by Django 4.1.4 on 2022-12-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='name',
            field=models.CharField(choices=[('kitchen', 'Kitchen'), ('bathroom', 'Bathroom'), ('bedroom', 'Bedroom'), ('living-room', 'Living Room')], max_length=50),
        ),
    ]
