# Generated by Django 3.1.4 on 2020-12-02 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('pessoa_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('endereco', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
    ]
