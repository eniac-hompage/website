# Generated by Django 3.2.7 on 2022-03-30 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_act_comment_activities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='comment',
        ),
    ]
