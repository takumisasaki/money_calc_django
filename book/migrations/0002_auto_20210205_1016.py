# Generated by Django 3.1.6 on 2021-02-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='good',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='read',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='readtext',
            field=models.TextField(blank=True, null=True),
        ),
    ]