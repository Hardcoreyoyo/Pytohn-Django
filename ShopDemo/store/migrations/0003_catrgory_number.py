# Generated by Django 2.2.6 on 2019-10-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20191011_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='catrgory',
            name='number',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]