# Generated by Django 2.0 on 2018-10-03 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0003_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='riddles',
        ),
        migrations.AddField(
            model_name='level',
            name='riddles',
            field=models.ManyToManyField(to='riddles.Riddles'),
        ),
    ]
