# Generated by Django 2.2.6 on 2019-12-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Child_police', '0008_auto_20191228_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policeregistrationmodel',
            name='complete_address',
            field=models.CharField(default=True, max_length=70),
        ),
    ]