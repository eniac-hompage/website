# Generated by Django 2.2.5 on 2022-02-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0010_auto_20220207_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='challenge_comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
