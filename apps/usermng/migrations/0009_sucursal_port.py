# Generated by Django 4.0.3 on 2022-03-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermng', '0008_alter_sucursal_operators'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='port',
            field=models.PositiveIntegerField(default=33306, max_length=5),
            preserve_default=False,
        ),
    ]
