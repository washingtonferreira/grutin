import re
from automata.tm.dtm import DTM

regex = '\{.*?\}'


def definicao_formal(def_formal):
    def_formal_padrao = re.findall(regex, def_formal)

    for i in range(len(def_formal_padrao)):
        def_formal_padrao[i] = def_formal_padrao[i].replace('{', '').replace('}', '').replace(' ', '').split(',')

    estados = def_formal_padrao[0]
    alfabeto = def_formal_padrao[1]
    simbolos_fita = def_formal_padrao[2]
    estado_inicial = def_formal_padrao[3][0]
    simbolo_branco = def_formal_padrao[4][0]
    estados_finais = def_formal_padrao[5]

    return estados, alfabeto, simbolos_fita, estado_inicial, simbolo_branco, estados_finais


def cria_funcao_transicao(estados, simbolos_fita):
    funcao_transicao = {}

    for e in estados:
        transicaoEstado = {}

        for s in simbolos_fita:
            transicao = input('({},{}): '.format(e, s))

            if transicao != '':
                transicaoEstado[s] = transicao.replace('(', '').replace(')', '').replace(' ', '').split(',')
        if len(transicaoEstado) != 0:
            funcao_transicao[e] = transicaoEstado

    return funcao_transicao


def cria_maq_turing(estados, alfabeto, simbolos_fita, funcao_transicao, est_inicial, simbolo_branco, est_finais):
    dtm = DTM(
        states=set(estados),
        input_symbols=set(alfabeto),
        tape_symbols=set(simbolos_fita),
        transitions=funcao_transicao,
        initial_state=est_inicial,
        blank_symbol=simbolo_branco,
        final_states=set(est_finais)
    )

    return dtm


def retorna_derivacao(mt, string_recebida):
    resultado = ''
    for state, tape in mt.validate_input(string_recebida, step=True):
        if resultado == '':
            resultado = state
            for t in tape.tape:
                resultado += t
        else:
            resultado += ' |- ' + state
            for t in tape.tape:
                resultado += t

    return resultado
