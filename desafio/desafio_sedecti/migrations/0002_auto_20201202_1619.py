# Generated by Django 3.1.4 on 2020-12-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio_sedecti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.CharField(max_length=2),
        ),
    ]
