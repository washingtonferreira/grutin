import re
from automata.fa.nfa import NFA

defFormal = input('Informe a Definição Formal do AFND: ')
defFormalPadrao = re.findall('\{.*?\}', defFormal)

for i in range(len(defFormalPadrao)):
    defFormalPadrao[i] = defFormalPadrao[i].replace('{', '').replace('}', '').replace(' ', '').split(',')

estados = set(defFormalPadrao[0])
alfabeto = set(defFormalPadrao[1])
estInical = defFormalPadrao[2][0]
estFinais = set(defFormalPadrao[3])
funcaoTransicao = {}

for e in estados:
    transicaoEstado = {}

    for a in alfabeto:
        if a == '':
            transicaoEstado[a] = input('Estado {} vendo {} vai para o Estado: '.format(e, 'vazio')).split(',')
        else:
            transicaoEstado[a] = input('Estado {} vendo {} vai para o Estado: '.format(e, a)).split(',')
    funcaoTransicao[e] = transicaoEstado

cadeia = input("Informe a cadeia: ") 

nfa = NFA(
    states=estados,
    input_symbols=alfabeto,
    transitions=funcaoTransicao,
    initial_state=estInical,
    final_states=estFinais
)

print(list(nfa.validate_input(cadeia, step=True)))

