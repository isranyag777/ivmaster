# Generated by Django 4.0.3 on 2022-03-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oprtid', models.CharField(max_length=3)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('ipaddress', models.CharField(max_length=12)),
            ],
        ),
    ]
