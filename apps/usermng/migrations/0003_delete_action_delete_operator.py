# Generated by Django 4.0.3 on 2022-03-17 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermng', '0002_action_operator'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.DeleteModel(
            name='Operator',
        ),
    ]
