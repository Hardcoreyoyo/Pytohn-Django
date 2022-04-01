# Generated by Django 2.2.6 on 2019-11-16 18:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='上傳時間'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='path',
            field=models.CharField(max_length=300, verbose_name='圖片路徑'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='story',
            field=models.TextField(verbose_name='圖片敘述'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=100, verbose_name='標題'),
        ),
    ]