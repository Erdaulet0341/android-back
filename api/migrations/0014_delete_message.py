# Generated by Django 4.2 on 2023-12-14 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_message_timestamp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]