import re
from automata.pda.dpda import DPDA


def definicaoFormal(defFormal):
    defFormalPadrao = re.findall('\{.*?\}', defFormal)

    for i in range(len(defFormalPadrao)):
        defFormalPadrao[i] = defFormalPadrao[i].replace('{', '').replace('}', '').replace(' ', '').split(',')

    estados = defFormalPadrao[0]
    alfabeto = defFormalPadrao[1] + ['']
    alfabetoPilha = defFormalPadrao[2]
    estInical = defFormalPadrao[3][0]
    simboloInicialPilha = defFormalPadrao[4][0]
    estFinais = defFormalPadrao[5]

    return estados, alfabeto, alfabetoPilha, estInical, simboloInicialPilha, estFinais


def getTransicao(estados, alfabeto, alfabetoPilha):
    transition = {}
    for s in estados:
        t1 = {}
        for sa in alfabeto:
            t2 = {}
            for ss in alfabetoPilha:
                c = input('({}, {}, {}) = '.format(s, sa, ss))
                c += ','

                c = c.replace(' ', '').split(',')
                d = tuple(c[1])
                if d == ():
                    d = ''
                if c[0] != '':
                    t2[ss] = (c[0], d)
            if t2 != {}:
                t1[sa] = t2
            if t1 != {}:
                transition[s] = t1

    return transition


def creatDPDA(estados, alfabeto, alfabetoPilha, transition, estInicial, initial_stack_symbol, estFinais):

    for i in range(len(alfabeto)):
        if alfabeto[i] == '':
            del alfabeto[i]

    return DPDA(
        states=set(estados),
        input_symbols=set(alfabeto),
        stack_symbols=set(alfabetoPilha),
        transitions=transition,
        initial_state=estInicial,
        initial_stack_symbol=initial_stack_symbol,
        final_states=set(estFinais)
    )


def showAutomatos(dpda, cadeia):
    print([(state, stack.copy()) for state, stack in dpda.validate_input(cadeia, step=True)])
