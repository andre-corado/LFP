import ply.lex as lex
from Clases import *

# Tokens
tokens = (
    'RESTILO',
    'ROPERACIONES',
    'RTIPO',
    'RTEXTO',
    'RTIPO2',
    'RTEXTO2',
    'RFUNCION',
    'RTITULO',
    'RDESCRIPCION',
    'RCONTENIDO',
    'ROPERACION',
    'RCOLOR',
    'RTAMANIO',
    'RNUMERO',
    'RSUMA',
    'RRESTA',
    'RMULTIPLICACION',
    'RDIVISION',
    'RINVERSO',
    'RPOTENCIA',
    'RRAIZ',
    'RSENO',
    'RCOSENO',
    'RMOD',
    'RTANGENTE',
    'RESCRIBIR',
    'LLAA',
    'LLAC',
    'IGUAL',
    'DIV',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CORA',
    'CORC',
    'RAZUL',
    'RVERDE',
    'RROJO',
    'RNEGRO',
    'RBLANCO',
    'RGRIS',
    'RCELESTE',
    'RCAFE',
)

# Lexemas
t_ignore = ' \t'
t_RESTILO = r'Estilo'
t_RTIPO2 = r'TIPO'
t_RTEXTO2 = r'TEXTO'
t_RTIPO = r'Tipo'
t_RTEXTO = r'Texto'
t_RFUNCION = r'Funcion'
t_RTITULO = r'Titulo'
t_RDESCRIPCION = r'Descripcion'
t_RCONTENIDO = r'Contenido'
t_ROPERACION = r'Operacion'
t_ROPERACIONES = r'Operaciones'
t_RCOLOR = r'Color'
t_RTAMANIO = r'Tamanio'
t_RSUMA = r'SUMA'
t_RRESTA = r'RESTA'
t_RMULTIPLICACION = r'MULTIPLICACION'
t_RDIVISION = r'DIVISION'
t_RMOD=r'MOD'
t_RINVERSO = r'INVERSO'
t_RPOTENCIA = r'POTENCIA'
t_RRAIZ = r'RAIZ'
t_RSENO = r'SENO'
t_RCOSENO = r'COSENO'
t_RTANGENTE = r'TANGENTE'
t_RESCRIBIR = r'ESCRIBIR'
t_RNUMERO = r'Numero'
t_LLAA = r'<'
t_LLAC = r'>'
t_IGUAL = r'='
t_DIV = r'/'
t_CORA = r'\['
t_CORC = r'\]'
t_RAZUL = r'AZUL'
t_RVERDE = r'VERDE'
t_RROJO = r'ROJO'
t_RNEGRO = r'NEGRO'
t_RBLANCO = r'BLANCO'
t_RGRIS = r'GRIS'
t_RCELESTE = r'CELESTE'
t_RCAFE = r'CAFE'


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


def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1]  # Se remueven las comillas de la entrada
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", "\'")
    t.value = t.value.replace('\\\\', '\\')
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
    '''instruccion  : INSTIPO
                    | INSTEXTO
                    | INSTFUNCION
                    | INSTESTILO


'''
    t[0] = t[1]


def p_instruccionTipo(t):
    'INSTIPO    :   LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLAC'
    t[0] = t[4]


def p_instruccionTexto(t):
    'INSTEXTO   :   LLAA RTEXTO LLAC CADENA LLAA DIV RTEXTO LLAC'
    t[0] = Texto(t[4], t.lineno(1), find_column(input, t.slice[1]))


def p_instruccionFuncion(t):
    'INSTFUNCION    :   LLAA RFUNCION IGUAL RESCRIBIR LLAC instrucciones_2 LLAA DIV RFUNCION LLAC'
    t[0] = Funcion(t[6][0], t[6][1], t[6][2], t.lineno(1), find_column(input, t.slice[1]))


def p_instruccionEstilo(t):
    'INSTESTILO     :   LLAA RESTILO LLAC instrucciones_2 LLAA DIV RESTILO LLAC'
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
    if len(t[6]) == 2:
        t[0] = Aritmeticas(t[6][0], t[6][1], t[4], t.lineno(1), find_column(input, t.slice[1]))
    else:
        t[0] = Aritmeticas(t[6][0], None, t[4], t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_2_decimal(t):
    'instruccion_2 : LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC '
    t[0] = Numero(float(t[4]), t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_2_entero(t):
    'instruccion_2 : LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC '
    t[0] = Numero(int(t[4]), t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_2_texto(t):
    'instruccion_2 : CADENA'
    t[0] = Numero(t[4], t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_2_titulo(t):
    'instruccion_2 : LLAA RTITULO LLAC ROPERACIONES LLAA DIV RTITULO LLAC'
    t[0] = t[4]


def p_instruccion_2_descripcion(t):
    'instruccion_2 : LLAA RDESCRIPCION LLAC CORA RTEXTO2 CORC LLAA DIV RDESCRIPCION LLAC'
    t[0] = t[5]


def p_instruccion_2_contenido(t):
    'instruccion_2 : LLAA RCONTENIDO LLAC CORA RTIPO2 CORC LLAA DIV RCONTENIDO LLAC'
    t[0] = t[5]


def p_instruccion_2_titulo_2(t):
    'instruccion_2 : LLAA RTITULO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_2_descripcion_2(t):
    'instruccion_2 : LLAA RDESCRIPCION RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_2_contenido_2(t):
    'instruccion_2 : LLAA RCONTENIDO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input, t.slice[1]))


def p_color(t):
    '''COLOR    : RAZUL
                | RVERDE
                | RROJO
                | RNEGRO
                | RBLANCO
                | RGRIS
                | RCELESTE
                | RCAFE'''
    t[0] = t[1]


def p_tipo(t):
    '''tipo :   RSUMA
            |   RRESTA
            |   RMULTIPLICACION
            |   RDIVISION
            |   RINVERSO
            |   RRAIZ
            |   RPOTENCIA
            |   RSENO
            |   RCOSENO
            |   RTANGENTE
            |   RMOD
    '''
    if t[1] == 'SUMA':
        t[0] = Operador.SUMA
    elif t[1] == 'RESTA':
        t[0] = Operador.RESTA
    elif t[1] == 'MULTIPLICACION':
        t[0] = Operador.MULTIPLICACION
    elif t[1] == 'DIVISION':
        t[0] = Operador.DIVISION
    elif t[1] == 'INVERSO':
        t[0] = Operador.INVERSO
    elif t[1] == 'RAIZ':
        t[0] = Operador.RAIZ
    elif t[1] == 'POTENCIA':
        t[0] = Operador.POTENCIA
    elif t[1] == 'SENO':
        t[0] = Operador.SENO
    elif t[1] == 'COSENO':
        t[0] = Operador.COSENO
    elif t[1] == 'TANGENTE':
        t[0] = Operador.TANGENTE
    elif t[1] == 'MOD':
        t[0] = Operador.MODULO


# Aqui reconoce un error de sintaxis, pueden crear un array e irlos agregando
# para obtenerlos después
def p_error(t):
    print("Error de sintaxis en '%s'" % t.value)


# Esta función busca la columna en la que se encuentra el token o lexema
def find_column(inp, tk):
    try:
        line_start = inp.rfind('\n', 0, tk.lexpos) + 1
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

    if variable:
        for var in variable:
            if isinstance(var, list):
                for var_ in var:
                    print(var_.ejecutar(True))
            elif isinstance(var, Texto):
                print(var.ejecutar(False))
            elif isinstance(var, Funcion):
                print(var.ejecutar(False))

    for var in errores_:
        print(var.toString())

    generarReportes()


def generarReportes():
    # Errores
    html = '''<h1 style="text-align: center;"><span style="text-decoration: underline;"><strong>ERRORES</strong></span><span style="text-decoration: underline;"><strong></strong></span><span style="text-decoration: underline;"><strong></strong></span></h1>
<p><span style="text-decoration: underline;"><strong></strong></span></p>'''
    num = 0
    if errores_.__len__() > 0:
        num += 1
        html += '''<table border="1" style="height: 45px; width: 84.2478%; border-collapse: collapse; margin-left: auto; margin-right: auto;">
<tbody>'''
        html += '''<tr style="height: 18px;"><td style="width: 20%s; text-align: center; height: 18px;">No.</td>
        <td style="width: 20%ds; text-align: center; height: 18px;">Lexema</td>
        <td style="width: 20%ds; text-align: center; height: 18px;">Tipo</td>
        <td style="width: 20%; text-align: center; height: 18px;">Columna</td>
        <td style="width: 20%; text-align: center; height: 18px;">Fila</td>
        </tr>'''
        for error in errores_:
            html += '''<tr style="height: 18px;">
<td style="width: 20%s; text-align: center; height: 18px;">''' + str(num) + '''</td>
<td style="width: 20%ds; text-align: center; height: 18px;">''' + error.lexema + '''</td>
<td style="width: 20%ds; text-align: center; height: 18px;">''' + error.tipo + '''</td>
<td style="width: 20%; text-align: center; height: 18px;">''' + str(error.columna) + '''</td>
<td style="width: 20%; text-align: center; height: 18px;">''' + str(error.fila) + '''</td>
</tr>'''
        html += '''</tbody>
    </table>'''
    else:
        html += '''<h2 style="text-align: center;">No se encontraron errores.</h2>
<table border="1" style="border-collapse: collapse; width: 100%; height: 36px;">'''
    f = open('ERRORES_202100154.html', 'w')
    f.write(html)

    # Resultados
    html2 = ''
    html2 += '<p style="text-align: center;">' + 'Operaciones' +  '<span style="font-size: 20pt; color: red;"></span></p>'
    contador = 0
    variable = parse(input)
    txtTitulo = colorTitulo = sizeTitulo = colorDesc = sizeDesc = colorContenido = sizeContenido = texto = None
    for var in variable:
        if isinstance(var, list):
            for var_ in var:
                if not(isinstance(var_, Aritmeticas)):
                    listaVar = var_.ejecutar(False)
                    if 'Titulo' in listaVar:
                        x2 = {'Titulo'}
                        x2 ^= listaVar
                        for x in x2:
                            if isinstance(x, str):
                                colorTitulo = traducirColor(x)
                            else:
                                sizeTitulo = str(x)
                    elif 'Descripcion' in listaVar:
                        x2 = {'Descripcion'}
                        x2 ^= listaVar
                        for x in x2:
                            if isinstance(x, str):
                                colorDesc = traducirColor(x)
                            else:
                                sizeDesc = str(x)
                    elif 'Contenido' in listaVar:
                        x2 = {'Contenido'}
                        x2 ^= listaVar
                        for x in x2:
                            if isinstance(x, str):
                                colorContenido = traducirColor(x)
                            else:
                                sizeContenido = str(x)

    for var in variable:
        if isinstance(var, list):
            for var_ in var:
                if isinstance(var_, Aritmeticas):
                    contador += 1
                    html2 += '<p style="text-align: center;">' + 'Operación No.' + str(contador) + '<span style="font-size:12pt; color: blue;"></span></p>'
                    html2 += '<p style="text-align: center;">' + str(var_.ejecutar(True)) + ' = ' + str(var_.ejecutar(False)) + '<span style="font-size: 12pt; color: blue;"></span></p>'


    f = open('RESULTADOS_202100154.html', 'w')
    f.write(html2)


def traducirColor(color):
    if color == 'ROJO':
        return 'RED'
    elif color == 'AZUL':
        return 'BLUE'
    elif color == 'VERDE':
        return 'GREEN'
    elif color == 'NEGRO':
        return 'BLACK'
    elif color == 'GRIS':
        return 'GRAY'
    elif color == 'CELESTE':
        return 'LIGHTBLUE'
    elif color == 'CAFE':
        return 'BROWN'
