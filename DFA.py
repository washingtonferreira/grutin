import re
from automata.fa.dfa import DFA

regex = '\{.*?\}'

definicaoFormal = input('Definição formal: ')

padrao = re.findall(regex, definicaoFormal)

for n in range(len(padrao)):
    padrao[n] = padrao[n].replace('{', '').replace('}', '').replace(' ', '').split(',')

states = set(padrao[0])
symbols = set(padrao[1])
initialState = padrao[2][0]
finalStates = set(padrao[3])

transition = {}

for state in states:
    dictionary = {}
    for s in symbols:
        dictionary[s] = input("Estado {} vendo {} vai para: ".format(state, s))
    transition[state] = dictionary

string = input('String: ')

dfa = DFA(
    states=states,
    input_symbols=symbols,
    transitions=transition,
    initial_state=initialState,
    final_states=finalStates
)

print(dfa.validate_input(string))
print(list(dfa.validate_input(string, step=True)))