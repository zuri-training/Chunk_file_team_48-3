# Generated by Django 4.0.6 on 2022-08-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_chunkedfile_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chunkedfile',
            name='upload_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
