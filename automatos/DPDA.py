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


def creatDPDA(states, alphabet, alphabetStack, transition, initialState, symbolsStackInitial, finalStates):

    for i in range(len(alphabet)):
        if alphabet[i] == '':
            del alphabet[i]

    return DPDA(
        states=set(states),
        input_symbols=set(alphabet),
        stack_symbols=set(alphabetStack),
        transitions=transition,
        initial_state=initialState,
        initial_stack_symbol=symbolsStackInitial,
        final_states=set(finalStates)
)


def returnAutomatos(dpda, cadeia):
    return str([(state, stack.copy()) for state, stack in dpda.validate_input(cadeia, step=True)])
