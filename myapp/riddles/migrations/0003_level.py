# Generated by Django 2.0 on 2018-10-03 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0002_auto_20181003_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('riddles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.Riddles')),
            ],
        ),
    ]
