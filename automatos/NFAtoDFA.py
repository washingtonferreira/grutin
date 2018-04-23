import re
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA

defFormal = input('Informe a Definição Formal do AFND: ')
defFormalPadrao = re.findall('\{.*?\}', defFormal)

for i in range(len(defFormalPadrao)):
    defFormalPadrao[i] = defFormalPadrao[i].replace('{', '').replace('}', '').replace(' ', '').split(',')

estados = defFormalPadrao[0]
alfabeto = defFormalPadrao[1]
estInical = defFormalPadrao[2][0]
estFinais = defFormalPadrao[3]
funcaoTransicao = {}

for e in estados:
    transicaoEstado = {}

    for a in alfabeto:
        if a == '':
            transicaoEstado[a] = input('Estado {} vendo {} vai para o Estado: '.format(e, 'vazio')).split(',')
        else:
            transicaoEstado[a] = input('Estado {} vendo {} vai para o Estado: '.format(e, a)).split(',')
        for t in transicaoEstado[a]:
            if t == '':
                transicaoEstado.pop(t)
    funcaoTransicao[e] = transicaoEstado

nfa = NFA(
    states=set(estados),
    input_symbols=set(alfabeto),
    transitions=funcaoTransicao,
    initial_state=estInical,
    final_states=set(estFinais)
)

dfa = DFA(nfa)

print('Automato Finito Deterministico gerado: {}'.format(dfa.states))

cadeia = input("Informe a cadeia: ")

print(list(dfa.validate_input(cadeia, step=True)))