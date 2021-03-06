# Generated by Django 3.1.5 on 2021-02-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20210203_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='location',
            name='ngi',
            field=models.ManyToManyField(blank=True, to='author.NarrativeGeneralInfo'),
        ),
        migrations.AlterField(
            model_name='narrativegeneralinfo',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='scene',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='world',
            name='name',
            field=models.CharField(default='', max_length=500),
        ),
    ]
