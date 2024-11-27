class BaseDeConhecimento:
    def __init__(self):
        self.fatos = {}
        self.regras = []

    def adicionar_fato(self, fato, valor):
        self.fatos[fato] = valor

    def adicionar_regra(self, regra):
        self.regras.append(regra)

    def obter_fatos(self):
        return self.fatos

    def obter_regras(self):
        return self.regras


class EngenhoDeInferencia:
    def __init__(self, base_de_conhecimento):
        self.base_de_conhecimento = base_de_conhecimento

    def inferir(self):
        fatos = self.base_de_conhecimento.obter_fatos()
        regras = self.base_de_conhecimento.obter_regras()

        for regra in regras:
            condicoes, diagnostico = regra.split('=>')
            condicoes = condicoes.split(',')
            if self.verificar_condicoes(condicoes, fatos):
                return diagnostico.strip()
        return "Diagnóstico não encontrado"

    def verificar_condicoes(self, condicoes, fatos):
        for condicao in condicoes:
            sintoma, valor = condicao.split('=')
            sintoma = sintoma.strip()
            valor = valor.strip()
            if fatos.get(sintoma) != valor:
                return False
        return True