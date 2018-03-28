from automata.fa.dfa import DFA

states = []
symbols = []
finalStates = []


qntState = int(input('Quantidade de estados: '))
qntSymbol = int(input('Quantidade de simbolos: '))
qntFinalState = int(input('Quantidade de estados finais: '))

initialState = input('Estado inicial: ')

for x in range(qntState):
    states.append(input('Nome do estado {}: '.format((x+1))))

for x in range(qntFinalState):
    finalStates.append(input('Nome do estado final: '))

for x in range(qntSymbol):
    symbols.append(input('Caractere do alfabeto: '))

transition = {}

states = set(states)
symbols = set(symbols)
finalStates = set(finalStates)


for state in states:
    dictionary = {}
    for s in symbols:
        dictionary[s] = input("Estado {} vendo {} vai para: ".format(state, s))
    transition[state] = dictionary

string = input("String: ")


dfa2 = DFA(
    states=states,
    input_symbols=symbols,
    transitions=transition,
    initial_state=initialState,
    final_states=finalStates
)

print(dfa2.validate_input(string))
print(list(dfa2.validate_input(string, step=True)))
