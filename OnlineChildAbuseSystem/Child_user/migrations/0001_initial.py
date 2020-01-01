# Generated by Django 2.2.6 on 2019-12-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplaintModel',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint_given_by', models.CharField(max_length=70)),
                ('from_address', models.TextField()),
                ('contact_number', models.CharField(max_length=70)),
                ('complaint_letter', models.TextField()),
                ('complaint_status', models.CharField(max_length=50)),
            ],
        ),
    ]
