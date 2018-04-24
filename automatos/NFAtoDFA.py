import re
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def definicao_formal(def_formal):
    def_formal_padrao = re.findall('\{.*?\}', def_formal)

    for i in range(len(def_formal_padrao)):
        def_formal_padrao[i] = def_formal_padrao[i].replace('{', '').replace('}', '').replace(' ', '').split(',')

    estados = def_formal_padrao[0]
    alfabeto = def_formal_padrao[1]
    estado_inical = def_formal_padrao[2][0]
    estados_finais = def_formal_padrao[3]

    return estados, alfabeto, estado_inical, estados_finais


def converter_nfa_dfa(estados, alfabeto, funcao_transicao, est_inicial, est_finais):
    nfa = NFA(
        states=set(estados),
        input_symbols=set(alfabeto),
        transitions=funcao_transicao,
        initial_state=est_inicial,
        final_states=set(est_finais)
    )

    dfa = DFA(nfa)

    return dfa


def retorna_estados(nfa, cadeia):
    print(list(nfa.validate_input(cadeia, step=True)))
