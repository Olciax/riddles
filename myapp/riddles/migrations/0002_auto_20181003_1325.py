# Generated by Django 2.0 on 2018-10-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='editimg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='editmail',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='editname',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='Pulpit/costam'),
        ),
        migrations.AlterField(
            model_name='riddles',
            name='hint',
            field=models.TextField(blank=True, null=True),
        ),
    ]