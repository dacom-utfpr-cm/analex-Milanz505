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
        'q61', 'q62', 'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70', 'q71'
        ],

        # Alfabeto
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
                '\n': 'q0',
                ' ': 'q0'},
            'q1': {'f': 'q2', 'n': 'q3', 'd': 'q5'},
            'q2': {' ': 'q0'},
            'q3': {'t': 'q4'},
            'q4': {' ': 'q0'},
            'q5': {' ': 'q0'},
            'q6': {'l': 'q7'},
            'q7': {'s': 'q8'},
            'q8': {'e': 'q9'},
            'q9': {' ': 'q0'},
            'q10': {'e': 'q11'},
            'q11': {'t': 'q12'},
            'q12': {'u': 'q13'},
            'q13': {'r': 'q14'},
            'q14': {'n': 'q15'},
            'q15': {' ': 'q0'},
            'q16': {'o': 'q17'},
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
            'q27': {' ': 'q0'},
            'q28': {' ': 'q0'},
            'q29': {' ': 'q0'},
            'q30': {' ': 'q0'},
            'q31': {' ': 'q32', '=': 'q33'},
            'q32': {' ': 'q0'},
            'q33': {' ': 'q0'},
            'q34': {' ': 'q0'},
            'q35': {' ': 'q0'},
            'q36': {' ': 'q0', 'v': 'q16'},
            'q37': {' ': 'q0', '{': 'q40'},
            'q38': {' ': 'q0'},
            'q39': {' ': 'q0'},
            'q40': {' ': 'q0', '\n': 'q0'},
            'q41': {' ': 'q0'},
            'q42': {' ': 'q0'},
            'q43': {'0': 'q43', '1': 'q43', '2': 'q43', '3': 'q43', '4': 'q43', '5': 'q43',
             '6': 'q43', '7': 'q43', '8': 'q43', '9': 'q43', '': 'q44'},
            'q44': {' ': 'q0'},
            'q45': {'a': 'q46'},
            'q46': {'i': 'q47'},
            'q47': {'n': 'q0'},
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
        'q28': 'DIVIDE\n',
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
        'q43': '',
        'q44': 'NUMBER\n',
        'q45': '',
        'q46': '',
        'q47': 'ID\n',
        'q48': '',
        'q49': '',
        'q50': '',
        'q51': '',
        'q52': '',
        'q53': '',
        'q54': '',
        },
)


def main():
    check_cm = False
    check_key = False
    
    for idx, arg in enumerate(sys.argv):
        # print("Argument #{} is {}".format(idx, arg))
        aux = arg.split('.')
        if aux[-1] == 'cm':
            check_cm = True
            idx_cm = idx

        if(arg == "-k"):
            check_key = True
    
    # print ("No. of arguments passed is ", len(sys.argv))

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
        
        print(moore.get_output_from_string(source_file))


if __name__ == "__main__":

    try:
        main()
    except Exception as e:
        print(e)
    except (ValueError, TypeError):
        print(e)