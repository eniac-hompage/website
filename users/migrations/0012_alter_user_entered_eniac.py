# Generated by Django 3.2.7 on 2022-02-15 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20220215_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='entered_eniac',
            field=models.SmallIntegerField(default=32, max_length=10),
        ),
    ]
