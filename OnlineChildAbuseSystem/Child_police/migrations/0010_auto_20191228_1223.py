# Generated by Django 2.2.6 on 2019-12-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Child_police', '0009_auto_20191228_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policeregistrationmodel',
            name='complete_address',
            field=models.TextField(default=True),
        ),
    ]
