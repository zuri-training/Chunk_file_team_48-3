# Generated by Django 4.0.6 on 2022-08-12 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_chunkedfile_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chunkedfile',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 12, 19, 33, 46, 574839)),
        ),
    ]
