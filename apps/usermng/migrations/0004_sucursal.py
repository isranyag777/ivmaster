# Generated by Django 4.0.3 on 2022-03-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermng', '0003_delete_action_delete_operator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ipadd', models.CharField(max_length=12)),
            ],
        ),
    ]
