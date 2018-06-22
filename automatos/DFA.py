import re
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

def convertToNFA(dfa):
    return NFA(dfa)

def definicaoFormal(defFormal):
    regex = '\{.*?\}'
    padrao = re.findall(regex, defFormal)

    for n in range(len(padrao)):
        padrao[n] = padrao[n].replace('{', '').replace('}', '').replace(' ', '').split(',')

    states = set(padrao[0])
    symbols = set(padrao[1])
    initialState = padrao[2][0]
    finalStates = set(padrao[3])

    return states, symbols, initialState, finalStates

def creatDFA(states, symbols, initialState, finalStates, transition):

    return DFA(
    states=states,
    input_symbols=symbols,
    transitions=transition,
    initial_state=initialState,
    final_states=finalStates
)

def showDFA(dfa, string):
    return list(dfa.validate_input(string, step=True))

def retornaNormaPadrao(dfa, inputStr):
    estadoI = dfa.initial_state
    transicao = dfa.transitions

    norma1 = '({}, {}) => {}'
    norma2 = '({}, ({}), {})'

    lista = list(dfa.validate_input(inputStr, step=True))
    lista.remove(lista[0])
    lista.reverse()
    strSaida = ''
    cutCount = 1

    for e in lista:
        inputAux = inputStr[-cutCount:]
        estadoAtual = transicao[e][inputAux]

        if inputStr[:-cutCount] != '':
            subNorma = norma2.format(e, inputStr[:-cutCount], inputAux, estadoAtual)
        else:
            subNorma = norma2.format(e, 'ε', inputAux, estadoAtual)

        strSaida += norma1.format(estadoI, subNorma, e) + '\n'
        inputStr = inputStr[:-cutCount]

    return strSaida
