# Generated by Django 3.2.7 on 2022-03-28 08:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20220319_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='developer',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='개발자'),
            preserve_default=False,
        ),
    ]
