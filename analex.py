from automata.fa.Moore import Moore
import sys, os

from myerror import MyError

error_handler = MyError('LexerErrors')

global check_cm
global check_key

moore = Moore(
    # States
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 
    'q11', 'q12', 'q012', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
    'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
    'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40',
    'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49','q50',
    'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60',
    'q61', 'q62', 'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70',
    'q71', 'q72', 'q73', 'q74', 'q75'
    ],

    # Alphabet
    [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '(', ')', '{', '}', ' ', '\n', '\t', '_', '0', '1', '2', '3', 
    '4', '5', '6', '7', '8', '9', ',', '+', '=', ';', ','
    ],

    # Outputs
    [
    'INT', 'IF', 'ELSE', 'RETURN', 'VOID', 'PLUS', 'MINUS', 'WHILE', 'TIMES', 'DIVIDE',
    'GREATER', 'LESS', 'DIFFERENT','ATTRIBUTION', 'EQUALS','COMMA','SEMICOLON',
    'LPAREN', 'RPAREN', 'LBRACKETS', 'RBRACKETS', 'LBRACES','RBRACES', 'NUMBER', 'ID'
    ],

    # State transitions
    {
        'q0': {
            'i': 'q1',
            'e': 'q6',
            'r': 'q10',
            'v': 'q16',
            '+': 'q20',
            '-': 'q21',
            'w': 'q22',
            '*': 'q27',
            '/': 'q28',
            '>': 'q29', 
            '<': 'q30',
            '=': 'q31',
            ',': 'q34',
            ';': 'q35',
            '(': 'q36',
            ')': 'q37',
            '[': 'q38',
            ']': 'q39',
            '{': 'q40',
            '}': 'q41',
            '0': 'q43',                
            '1': 'q43','2': 'q43','3': 'q43','4': 'q43','5': 'q43','6': 'q43','7': 'q43','8': 'q43','9': 'q43',
            'm': 'q45',
            'x': 'q48', 'y': 'q48', 'a': 'q48', 'b': 'q48', 'c': 'q48','u': 'q48','z': 'q48',
            'f': 'q49',
            's': 'q53',
            'o': 'q58',
            'g': 'q63',   
            '!': 'q74',
            '\n': 'q0',
            ' ': 'q0'},
        'q1': {'f': 'q2', 'n': 'q3', 'd': 'q5'},
        'q2': {' ': 'q0', '(': 'q36'},
        'q3': {'t': 'q4', 'p': 'q56'},
        'q4': {' ': 'q0'},
        'q5': {' ': 'q0'},
        'q6': {'l': 'q7'},
        'q7': {'s': 'q8'},
        'q8': {'e': 'q9'},
        'q9': {' ': 'q0'},
        'q10': {'e': 'q11'},
        'q11': {'t': 'q12','s': 'q73'},
        'q12': {'u': 'q13'},
        'q13': {'r': 'q14'},
        'q14': {'n': 'q15'},
        'q15': {' ': 'q0', '(': 'q36',  ';': 'q35'},
        'q16': {'o': 'q17',')':'q67',';':'q68', ' ': 'q48', ',':'q69'},
        'q17': {'i': 'q18'},
        'q18': {'d': 'q0'},
        'q19': {' ': 'q0'},
        'q20': {' ': 'q0'},
        'q21': {' ': 'q42', '0': 'q43', '1': 'q43', '2': 'q43', '3': 'q43', '4': 'q43', '5': 'q43',
         '6': 'q43', '7': 'q43', '8': 'q43', '9': 'q43'},
        'q22': {'h': 'q23'},
        'q23': {'i': 'q24'},
        'q24': {'l': 'q25'},
        'q25': {'e': 'q26'},
        'q26': {' ': 'q0'},
        'q27': {' ': 'q0','v': 'q48'},
        'q28': {' ': 'q65','*': 'q66'},
        'q29': {' ': 'q0'},
        'q30': {' ': 'q0'},
        'q31': {' ': 'q32', '=': 'q33'},
        'q32': {' ': 'q0','i': 'q1','s': 'q53', 'x': 'q48', '-': 'q21', 'a': 'q48','b': 'q48', 'f': 'q49', '1': 'q43'},
        'q33': {' ': 'q0'},
        'q34': {' ': 'q0','y': 'q48','u': 'q48', 'b': 'q48'},
        'q35': {' ': 'q0','\n': 'q0', '}' : 'q41'},
        'q36': {' ': 'q0','g':'q63', 'v': 'q16','i': 'q1' ,')': 'q37','x': 'q48','z': 'q48', 'r': 'q10', 'a': 'q48','c': 'q48',
                '0': 'q43', '1': 'q43', '2': 'q43', '3': 'q43', '4': 'q43', '5': 'q43','6': 'q43', '7': 'q43', '8': 'q43', '9': 'q43'},
        'q37': {' ': 'q0', '{': 'q40', ';' : 'q35', ')': 'q37'},
        'q38': {' ': 'q0','0': 'q43', '1': 'q43', '2': 'q43', '3': 'q43', '4': 'q43',
        '5': 'q43', '6': 'q43', '7': 'q43', '8': 'q43', '9': 'q43'},
        'q39': {' ': 'q0', ';': 'q35', '[': 'q38', ')': 'q37'},
        'q40': {' ': 'q0', '\n': 'q0'},
        'q41': {' ': 'q0', '\n': 'q0'},
        'q42': {' ': 'q0','u': 'q48', '0': 'q43', '1': 'q43', '2': 'q43', '3': 'q43', '4': 'q43','5': 'q43', '6': 'q43', '7': 'q43', '8': 'q43', '9': 'q43'},
        'q43': {'0': 'q43', '1': 'q43', '2': 'q43', '3': 'q43', '4': 'q43','5': 'q43', '6': 'q43', '7': 'q43', '8': 'q43', '9': 'q43',
                ')': 'q37', ';': 'q35', ']': 'q39', ',': 'q34', '\n': 'q0'},
        'q44': {' ': 'q0'},
        'q45': {'a': 'q46'},
        'q46': {'i': 'q47'},
        'q47': {'n': 'q0'},
        'q48': {' ': 'q0', ',': 'q34', ';': 'q35', ')': 'q37','/': 'q65','+': 'q20','-': 'q42','*': 'q27', '=': 'q31','[': 'q38'},
        'q49': {'l':'q50', 'u':'q71'},
        'q50': {'o':'q51'},
        'q51': {'a':'q52'},
        'q52': {'t':'q0'},
        'q53': {'o': 'q54'},        
        'q54': {'m': 'q55'},
        'q55': {'a': 'q0'},
        'q56': {'u': 'q57'},
        'q57': {'t': 'q0'},
        'q58': {'u': 'q59'},
        'q59': {'t': 'q60'},
        'q60': {'p': 'q61'},
        'q61': {'u': 'q62'},
        'q62': {'t': 'q0'},
        'q63': {'c': 'q64'},
        'q64': {'d': 'q0'},
        'q65': {' ': 'q0','v': 'q48'},
        'q66': { #COMENTAAAAAAAAAAAAAAAA
            '\n': 'q66',
            ' ': 'q66',
            'u': 'q66',
            '-': 'q66',
            '/': 'q66',
            'v': 'q66',
            '=': 'q66',
            'm': 'q66',
            'o': 'q66',
            'd': 'q66',
            '*': 'q70',
        },
        'q67': {' ': 'q0', '{':'q40'},
        'q68': {' ': 'q0', '\n': 'q0'},
        'q69': {' ': 'q0', 'u': 'q48'},
        'q70': {
            '/': 'q0',
            'v': 'q66',
        },
        'q71': {'n': 'q72'},
        'q72': {'c': 'q0'},
        'q73': {' ': 'q0',';': 'q35', ')': 'q37'},
        'q74': {' ': 'q0', '=': 'q75'},
        'q75': {' ': 'q0'},
    }, 

    # Initial State
    'q0',

    # Output de State
    {
    'q0': '',
    'q1': '',
    'q2': 'IF\n',
    'q3': '',
    'q4': 'INT\n',
    'q5': 'ID\n',
    'q6': '',
    'q7': '',
    'q8': '',
    'q9': 'ELSE\n',
    'q10': '',
    'q11': '',
    'q12': '',
    'q13': '',
    'q14': '',
    'q15': 'RETURN\n',
    'q16': '',
    'q17': '',
    'q18': 'VOID\n',
    'q19': '',
    'q20': 'PLUS\n',
    'q21': '',
    'q22': '',
    'q23': '',
    'q24': '',
    'q25': '',
    'q26': 'WHILE\n',
    'q27': 'TIMES\n',
    'q28': '',
    'q29': 'GREATER\n',
    'q30': 'LESS\n',
    'q31': '',
    'q32': 'ATTRIBUTION\n',
    'q33': 'EQUALS\n',
    'q34': 'COMMA\n',
    'q35': 'SEMICOLON\n',
    'q36': 'LPAREN\n',
    'q37': 'RPAREN\n',
    'q38': 'LBRACKETS\n',
    'q39': 'RBRACKETS\n',
    'q40': 'LBRACES\n',
    'q41': 'RBRACES\n',
    'q42': 'MINUS\n',
    'q43': 'NUMBER\n',
    'q44': '',
    'q45': '',
    'q46': '',
    'q47': 'ID\n',
    'q48': 'ID\n',
    'q49': '',
    'q50': '',
    'q51': '',
    'q52': 'FLOAT\n',
    'q53': '',
    'q54': '',
    'q55': 'ID\n',
    'q56': '',
    'q57': 'ID\n',
    'q58': '',
    'q59': '',
    'q60': '',
    'q61': '',
    'q62': 'ID\n',
    'q63': '',
    'q64': 'ID\n',
    'q65': 'DIVIDE\n',
    'q66': '',
    'q67': 'ID\n' 'RPAREN\n',
    'q68': 'ID\n' 'SEMICOLON\n',
    'q69': 'ID\n' 'COMMA\n',
    'q70': '',
    'q71': '',
    'q72': 'ID\n',
    'q73': 'ID\n',
    'q74': '',
    'q75': 'DIFFERENT\n',
    },
)

import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    check_cm = False
    check_key = False
    
    for idx, arg in enumerate(sys.argv):
        aux = arg.split('.')
        if aux[-1] == 'cm':
            check_cm = True
            idx_cm = idx

        if(arg == "-k"):
            check_key = True
    
    if(len(sys.argv) < 3):
        raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

    if not check_cm:
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
    elif not os.path.exists(sys.argv[idx_cm]):
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
    else:
        data = open(sys.argv[idx_cm])
        source_file = data.read()

        if not check_cm:
            print("Definição da Máquina")
            print(moore)
            print("Entrada:")
            print(source_file)
            print("Lista de Tokens:")
        
        # Debugging
        current_state = 'q0'
        output = []
        debug_logs = []

        for char in source_file:
            if char in moore.transitions[current_state]:
                next_state = moore.transitions[current_state][char]
                debug_logs.append(f"Transition: {current_state} --({char})--> {next_state}")  # Guardar logs em vez de imprimir
                current_state = next_state
                output.append(moore.output_table[current_state])
            else:
                debug_logs.append(f"Unexpected character '{char}' in state '{current_state}'")
                break

        # print("\n".join(debug_logs))

        print("".join(output))  


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
    except (ValueError, TypeError):
        print(e) 