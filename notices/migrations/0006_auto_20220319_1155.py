# Generated by Django 2.2.5 on 2022-03-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0005_auto_20220313_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]