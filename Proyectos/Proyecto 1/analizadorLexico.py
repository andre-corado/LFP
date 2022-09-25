import ply.lex as lex
import re
import codecs
import os
import sys
from Clases import Error

# Tokens
tokens = ['RESTILO', 'ROPERACIONES', 'RTIPO',
          'RTEXTO', 'RTIPO2', 'RTEXTO2',
          'RFUNCION', 'RTITULO', 'RDESCRIPCION',
          'RCONTENIDO', 'ROPERACION', 'RCOLOR',
          'RTAMANIO', 'RNUMERO', 'RSUMA',
          'RRESTA', 'RMULTIPLICACION', 'RDIVISION',
          'RINVERSO', 'RESCRIBIR', 'LLAA', 'LLAC',
          'IGUAL', 'DIV', 'ENTERO',
          'DECIMAL', 'CADENA', 'CORA',
          'CORC', 'RAZUL', 'RVERDE', 'RROJO',
          'RNEGRO', 'RBLANCO', 'RGRIS',
          'RCELESTE', 'RCAFE'
          ]

# Lexemas
t_IGNORAR = ' \t'
t_RESTILO = r'Estilo'
t_RTIPO = r'Tipo'
t_RTEXTO = r'Texto'
t_RTIPO2 = r'TIPO'
t_RTEXTO2 = r'TEXTO'
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
t_RINVERSO = r'INVERSO'
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
    r'\d+\-\d+'
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


def t_nuevaLinea(t):
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

archivo = open('analizador.txt', 'r')
global input
global errores_
errores_ = []
input = archivo.read()
archivo.close()
