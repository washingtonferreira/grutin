import re
from automata.fa.dfa import DFA

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
