import re
from automata.tm.dtm import DTM

regex  = '\{.*?\}'
defFormal = input('Informe a Definição Formal da Máquina de Turing: ')
defFormalPadrao = re.findall(regex, defFormal)

for i in range(len(defFormalPadrao)):
    defFormalPadrao[i] = defFormalPadrao[i].replace('{', '').replace('}', '').replace(' ', '').split(',')

estados = defFormalPadrao[0]
alfabeto = defFormalPadrao[1]
simbolosFita = defFormalPadrao[2]
estadoInicial = defFormalPadrao[3][0]
simboloBranco = defFormalPadrao[4][0]
estadosFinais = defFormalPadrao[5]
funcaoTransicao = {}

for e in estados:
    transicaoEstado = {}

    for s in simbolosFita:
        transicao = input('({},{}): '.format(e, s))

        if transicao != '':
            transicaoEstado[s] = transicao.replace('(', '').replace(')', '').replace(' ', '').split(',')
    if len(transicaoEstado) != 0:
        funcaoTransicao[e] = transicaoEstado

#print(funcaoTransicao)

dtm = DTM(
    states=set(estados),
    input_symbols=set(alfabeto),
    tape_symbols=set(simbolosFita),
    transitions=funcaoTransicao,
    initial_state=estadoInicial,
    blank_symbol=simboloBranco,
    final_states=set(estadosFinais)
)

stringRecebida = input('Informe a string: ')

resultado = ''

for state, tape in dtm.validate_input(stringRecebida, step=True):
    if resultado == '':
        resultado = state
        for t in tape.tape:
            resultado += t
    else:
        resultado += ' |- ' + state
        for t in tape.tape:
            resultado += t

print(resultado)
