# Generated by Django 3.2.7 on 2022-02-07 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0009_auto_20220207_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='challenge_comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
