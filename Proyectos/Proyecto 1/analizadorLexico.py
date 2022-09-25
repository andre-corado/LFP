import ply.lex as lex
from Clases import *

# Tokens
tokens = (
    'RTIPO',
    'ROPERACION',
    'RNUMERO',
    'RSUMA',
    'RRESTA',
    'RMULTIPLICACION',
    'RDIVISION',
    'LLAA',
    'LLAC',
    'IGUAL',
    'DIV',
    'ENTERO',
    'DECIMAL',
)

# Lexemas
t_ignore = ' \t'
t_RTIPO       = r'Tipo'
t_ROPERACION  = r'Operacion'
t_RSUMA       = r'SUMA'
t_RRESTA       = r'RESTA'
t_RMULTIPLICACION = r'MULTIPLICACION'
t_RDIVISION = r'DIVISION'
t_RNUMERO     = r'Numero'
t_LLAA        = r'<'
t_LLAC        = r'>'
t_IGUAL       = r'='
t_DIV         = r'/'


# Gramática para números

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal demasiado largo %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero demasiado largo %d", t.value)
        t.value = 0
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Error Léxico
def t_error(t):
    print("Error Léxico, no se reconoce: '%s'" % t.value[0])
    error = Error(t.value[0], 'Error Lexico', t.lineno, find_column(input, t))
    errores_.append(error)
    t.lexer.skip(1)


# Esta función busca la columna en la que se encuentra el token o lexema
def find_column(inp, tk):
    try:
        line_start = inp.rfind('\n', 0, tk.lexpos) + 1
        return (tk.lexpos - line_start) + 1
    except:
        return 0


# Analizador léxico
lexer = lex.lex()



# ANALIZADOR SINTACTICO
# Definicion de la gramatica

def p_init(t):
    'init : instrucciones'
    t[0] = t[1]
    return t[0]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        |   instruccion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruccion(t):
    'instruccion  : LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLAC'
    t[0] = t[4]

def p_instrucciones_2_lista(t):
    'instrucciones_2 : instrucciones_2 instruccion_2'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2_instruccion(t):
    'instrucciones_2 :  instruccion_2'
    t[0] = [t[1]]

def p_instruccion_2(t):
    'instruccion_2  :  LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLAC'
    t[0] = Aritmeticas(t[6][0], t[6][1], t[4], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_decimal(t):
    'instruccion_2 : LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC '
    t[0] = Numero(float(t[4]), t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_entero(t):
    'instruccion_2 : LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC '
    t[0] = Numero(int(t[4]), t.lineno(1), find_column(input,t.slice[1]))

def p_tipo(t):
    '''tipo :   RSUMA
            |   RRESTA
            |   RMULTIPLICACION
            |   RDIVISION
    '''
    if t[1] == 'SUMA':
        t[0] = Operador.SUMA
    elif t[1] == 'RESTA':
        t[0] = Operador.RESTA
    elif t[1] == 'MULTIPLICACION':
        t[0] = Operador.MULTIPLICACION
    elif t[1] == 'DIVISION':
        t[0] = Operador.DIVISION

# Aqui reconoce un error de sintaxis, pueden crear un array e irlos agregando
# para obtenerlos después
def p_error(t):
    print("Error de sintaxis en '%s'" % t.value)

# Esta función busca la columna en la que se encuentra el token o lexema
def find_column(inp, tk):
    try:
        line_start = inp.rfind('\n',0,tk.lexpos) + 1
        return (tk.lexpos - line_start) + 1
    except:
        return 0

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    lexer.lineno = 1
    return parser.parse(input)

genAux = Generador()
generador = genAux.getInstance()


def analizar(texto):
    global input
    global errores_
    errores_ = []
    input = texto
    variable = parse(input)
    getER = True

    for var in variable:
        for var_ in var:
            print(var_.ejecutar(getER))

    for var in errores_:
        print(var.toString())

