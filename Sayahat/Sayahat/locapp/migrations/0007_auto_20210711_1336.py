# Generated by Django 3.1.2 on 2021-07-11 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locapp', '0006_remove_destinationcitydetails_destination_extras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationcitydetails',
            name='destination_desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='destinationmetadetails',
            name='meta_destination_desc',
            field=models.TextField(),
        ),
    ]
