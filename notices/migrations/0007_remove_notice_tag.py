# Generated by Django 3.2.7 on 2022-02-04 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0006_alter_notice_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='tag',
        ),
    ]