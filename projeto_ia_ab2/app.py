from diagnostico import BaseDeConhecimento, EngenhoDeInferencia

base_de_conhecimento = BaseDeConhecimento()
base_de_conhecimento.adicionar_fato('dor_de_cabeca', 'sim')
base_de_conhecimento.adicionar_fato('garganta_inflamada', 'sim')
base_de_conhecimento.adicionar_fato('tosse', 'sim')

base_de_conhecimento.adicionar_regra('dor_de_cabeca=sim, garganta_inflamada=sim, tosse=sim => diagnostico=gripe')
base_de_conhecimento.adicionar_regra('dor_de_cabeca=sim, garganta_inflamada=nao, tosse=nao => diagnostico=enxaqueca')

engenho_de_inferencia = EngenhoDeInferencia(base_de_conhecimento)
diagnostico = engenho_de_inferencia.inferir()
print(diagnostico)  # Saída: diagnostico=gripe
