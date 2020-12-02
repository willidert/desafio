from django.db import models


class Pessoa(models.Model):

    SEXO_OPCS = (
        ('M', u'Masculino'),
        ('F', u'Feminino')
        )

    pessoa_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=2)
    sexo = models.CharField(choices=SEXO_OPCS, max_length=1)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nome
