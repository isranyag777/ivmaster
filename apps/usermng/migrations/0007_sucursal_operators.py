# Generated by Django 4.0.3 on 2022-03-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermng', '0006_rename_ipadd_sucursal_ipaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='sucursal',
            name='operators',
            field=models.CharField(default='operator', max_length=200),
        ),
    ]