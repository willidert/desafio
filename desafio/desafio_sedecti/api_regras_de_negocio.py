class RegrasNegocioAvaliador:
    """docstring for RegrasNegocioAvaliador"""
    def run(self, campos):
        return all([
            self.validar_cpf(campos["cpf"]),
            self.validar_nome(campos["nome"]),
            self.validar_endereco(campos["endereco"]),
            self.validar_sexo(campos["sexo"]),
            self.validar_idade(campos["idade"]),
            ])

    def validar_cpf(self, cpf):
        soma = 0
        resto = 0

        if len(cpf) != 11 or len(set(cpf)) < 1:
            # 00000000000 -> 111... 999
            return False

        soma = sum([(i) * int(cpf[10 - i]) for i in range(10, 1, -1)])
        resto = (soma*10) % 11

        if resto == 10:
            resto = 0

        if int(cpf[9]) != resto:
            return False

        soma = sum([(i) * int(cpf[11-i]) for i in range(11, 1, -1)])
        resto = soma*10 % 11

        if resto == 10 or resto == 11:
            resto = 0

        if int(cpf[10]) != resto:
            return False

        return True

    def validar_nome(self, nome):
        import string

        PERMITIDAS_INICIO = list(string.ascii_uppercase)
        PERMITIDAS_MEIO = list(string.ascii_letters) + [" "]

        if nome[0] in PERMITIDAS_INICIO:
            for i in set(nome):
                if i not in PERMITIDAS_MEIO:
                    return False
            return True
        return False

    def validar_endereco(self, endereco):
        import string

        PERMITIDAS_INICIO = list(string.ascii_uppercase)
        PONTUACAO = list(string.punctuation)
        PERMITIDAS_MEIO = list(string.ascii_letters) + list(string.digits) + [" "] + PONTUACAO

        if endereco[0] in PERMITIDAS_INICIO:
            for i in range(len(endereco)):
                if (endereco[i] not in PERMITIDAS_MEIO or (i < (len(endereco)-1) and (endereco[i] in PONTUACAO) and (endereco[i+1] in PONTUACAO))):
                    return False
            return True
        return False

    def validar_idade(self, idade):
        return True if len(str(idade)) <= 2 else False

    def validar_sexo(self, sexo):
        PERMITIDOS = ["M", "F"]
        return True if len(sexo) == 1 and sexo in PERMITIDOS else False
