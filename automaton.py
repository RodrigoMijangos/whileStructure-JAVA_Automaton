import re


def automaton(state=None, chain=None, i=0):

    state_changed = False

    final_states = ["INSF"]
    transitions = {
        "INI": [
            ['[w]', "W1"]
        ],
        "W1": [
            ['[h]', "W2"]
        ],
        "W2": [
            ['[i]', "W3"]
        ],
        "W3": [
            ['[l]', "W4"]
        ],
        "W4": [
            ['[e]', "P1"]
        ],
        "P1": [
            ['[(]', "INIVA_1"],
        ],
        "INIVA_1": [
            ['[a-zA-Z]', "VA1_1"],
            ['[1-9]', "N1_1"],
            ['[0]', "N0_1"]
        ],
        "VA1_1": [
            ['[a-zA-Z0-9]', "VA1_1"],
            ['[_]', "VA2_1"],
            ['[=!]', "CON1"],
            ['[<>]', "CON2"]
        ],
        "VA2_1": [
            ['[A-Za-z0-9]', "VA1_1"],
        ],
        "N1_1": [
            ['[0-9]', "N1_1"],
            ['[=!]', "CON1"],
            ['[<>]', "CON2"]
        ],
        "NO_1":[
            ['[=!]', "CON1"],
            ['[<>]', "CON2"]
        ],
        "CON1": [
            ['[=]', "INIVA_2"]
        ],
        "CON2": [
            ['[=]', "INIVA_2"],
            ['[A-Za-z]', "VA1_2"],
            ['[1-9]', "N1_2"],
            ['[0]', "N0_2"]
        ],
        "INIVA_2": [
            ['[A-Za-z]', "VA1_2"],
            ['[1-9]', "N1_2"],
            ['[0]', "N0_2"]
        ],
        "VA1_2": [
            ['[a-zA-Z0-9]', "VA1_2"],
            ['[_]', "VA2_2"],
            ['[)]', "P2"]
        ],
        "VA2_2": [
            ['[A-Za-z0-9]', "VA1_2"]
        ],
        "N0_2": [
            ['[)]', "P2"]
        ],
        "N1_2": [
            ['[0-9]', "N1_2"],
            ['[)]', "P2"]
        ],
        "P2": [
            ['[{]', "INIVA_3"]
        ],
        "INIVA_3": [
            ['[A-Za-z]', "VA1_3"],
            ['[}]', "INSF"],
            ['[\t\n]', "INIVA_3"]
        ],
        "VA1_3": [
            ['[A-Za-z0-9]', "VA1_3"],
            ['[_]', "VA2_3"],
            ['[=]', "INIVA_4"]
        ],
        "VA2_3": [
            ['[A-Za-z0-9]', "VA1_3"],
        ],
        "INIVA_4": [
            ['[a-zA-Z]', "VA1_4"],
            ['[1-9]', "N1_4"],
            ['[0]', "N0_4"]
        ],
        "VA1_4": [
            ['[a-zA-Z0-9]', "VA1_4"],
            ['[_]', "VA2_4"],
            ['[+-/*]', "INIVA_5"]
        ],
        "VA2_4": [
            ['[A-Za-z0-9]', "VA1_4"],
        ],
        "N1_4": [
            ['[0-9]', "N1_4"],
            ['[+-/*]', "INIVA_5"]
        ],
        "N0_4": [
            ['[+-/*]', "INIVA_5"]
        ],
        "INIVA_5": [
            ['[a-zA-Z]', "VA1_5"],
            ['[1-9]', "N1_5"],
            ['[0]', "N0_5"]

        ],
        "VA1_5": [
            ['[a-zA-Z0-9]', "VA1_5"],
            ['[_]', "VA2_5"],
            ['[;]', "INS2"]
        ],
        "VA2_5": [
            ['[A-Za-z0-9]', "VA1_5"],
        ],
        "N0_5": [
            ['[;]', "INS2"]
        ],
        "N1_5": [
            ['[0-9]', "N1_5"],
            ['[;]', "INS2"]
        ],
        "INS2": [
            ['[\n]', "INIVA_3"],
            ['[}]', "INSF"]
        ]
    }

    if state is None:
        state = "INI"

    actual_eval = transitions[state]
    state_log = f"Entry: {chain[i]}, Actual State: {state}"
    for transition in actual_eval:

        if re.search(transition[0], chain[i]) is not None:
            state = transition[1]
            state_changed = True
            state_log += f" New State: {state}"
            break
    if not state_changed:
        state_log += f" Transition Failed"
        print(state_log)
        return False
    elif i + 1 == len(chain):
        print(state_log)
        if state in final_states:
            return True
        else:
            return False
    print(state_log)
    i += 1
    return automaton(state, chain, i)
