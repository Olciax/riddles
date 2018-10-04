# Generated by Django 2.0 on 2018-10-04 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0004_auto_20181003_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curiosity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='Pulpit/costam')),
            ],
        ),
        migrations.CreateModel(
            name='CuriosityQA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterModelOptions(
            name='riddles',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='myuser',
            name='donecur',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='curiosity',
            name='curiosityQA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riddles.CuriosityQA'),
        ),
    ]