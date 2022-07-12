# Generated by Django 4.0.4 on 2022-07-12 10:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.AlterModelOptions(
            name='detail',
            options={'ordering': ('pk',)},
        ),
        migrations.AddField(
            model_name='detail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 7, 12, 10, 17, 26, 491775, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
