# Generated by Django 3.1.5 on 2021-01-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_auto_20210115_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='chapter',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chapter',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='character',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='character',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='location',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='scene',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='scene',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='world',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]