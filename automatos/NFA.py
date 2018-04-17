import re
from automata.fa.nfa import NFA


def definicaoFormal(defFormal):
    defFormalPadrao = re.findall('\{.*?\}', defFormal)

    for i in range(len(defFormalPadrao)):
        defFormalPadrao[i] = defFormalPadrao[i].replace('{', '').replace('}', '').replace(' ', '').split(',')

    estados = set(defFormalPadrao[0])
    alfabeto = set(defFormalPadrao[1])
    estInical = defFormalPadrao[2][0]
    estFinais = set(defFormalPadrao[3])

    return estados, alfabeto, estInical, estFinais


def getTransicao(estados, alfabeto):
    funcaoTransicao = {}

    for e in estados:
        transicaoEstado = {}

        for a in alfabeto:
            if a == '':
                transicaoEstado[a] = (input('Estado {} vendo {} vai para o Estado: '.format(e, 'vazio'))
                                      .replace(' ', '').split(','))
            else:
                transicaoEstado[a] = (input('Estado {} vendo {} vai para o Estado: '.format(e, a))
                                      .replace(' ', '').split(','))

            for t in transicaoEstado[a]:
                if t == '':
                    transicaoEstado.pop(t)

        funcaoTransicao[e] = transicaoEstado

    return funcaoTransicao


def removeUnusableStates(transicaoEstado):
    transicaoEstado = dict(transicaoEstado)
    print(transicaoEstado)
    print('Chaves: ', transicaoEstado.keys())
    print('Valores: ', transicaoEstado.values())

    for key in transicaoEstado:
        value = (transicaoEstado.get(key))
        if value == {''}:
            print(value)
    return transicaoEstado


def creatNFA(estados, alfabeto, funcaoTransicao, estInicial, estFinais):
    return NFA(
        states=estados,
        input_symbols=alfabeto,
        transitions=funcaoTransicao,
        initial_state=estInicial,
        final_states=estFinais
    )


def showAutomatos(nfa, cadeia):
    print(list(nfa.validate_input(cadeia, step=True)))
