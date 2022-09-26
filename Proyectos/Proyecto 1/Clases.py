from enum import Enum
from abc import ABC, abstractmethod
import math


class Expression(ABC):

    def __init__(self, fila, column):
        self.fila = fila
        self.column = column

    @abstractmethod
    def ejecutar(self, getER):
        pass


class Error:
    def __init__(self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna
        self.fila = fila

    def toString(self):
        return f"=======\nLexema: {self.lexema}\nTipo: {self.tipo}\nColumna: {self.columna}\nFila: {self.fila}\n======="


class Operador(Enum):
    OPERACION = 0
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    POTENCIA = 5
    MODULO = 6
    INVERSO = 7
    TANGENTE = 8
    COSENO = 9
    SENO = 10
    RAIZ = 11


class Generador:
    generador = None

    def getInstance(self):
        if Generador.generador is None:
            Generador.generador = Generador()
        return Generador.generador

    def addExpresion(self, n1, n2, tipo):
        return f'({n1} {tipo} {n2})'

    def addTrigonometrica(self, n1, tipo):
        return f'{tipo}({n1})'


class Aritmeticas(Expression):

    def __init__(self, left, right, tipo, fila, column):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, column)

    def ejecutar(self, getER):
        genAux = Generador()
        generador = genAux.getInstance()

        izq = self.left.ejecutar(getER)
        if self.right != None:
            der = self.right.ejecutar(getER)
            if self.tipo == Operador.SUMA:
                return generador.addExpresion(izq, der, '+') if getER else izq + der
            elif self.tipo == Operador.RESTA:
                return generador.addExpresion(izq, der, '-') if getER else izq - der
                # return izq - der
            elif self.tipo == Operador.MULTIPLICACION:
                return generador.addExpresion(izq, der, '*') if getER else izq * der
                # return izq * der
            elif self.tipo == Operador.DIVISION:
                if der != 0:
                    return generador.addExpresion(izq, der, '/') if getER else izq / der
                    # return izq / der
                else:
                    print("Error: Division por cero")
                    return None
            elif self.tipo == Operador.POTENCIA:
                return generador.addExpresion(izq, der, '^') if getER else izq ** der
                # return izq ** der
            elif self.tipo == Operador.MODULO:
                return generador.addExpresion(izq, der, '%') if getER else izq % der
                # return izq % derS
            elif self.tipo == Operador.RAIZ:
                return generador.addExpresion(izq, der, 'raiz') if getER else izq ** (1 / der)
                # return izq**(1/der)
            else:
                return 0
        else:
            if self.tipo == Operador.INVERSO:
                return generador.addExpresion(1, izq, '/') if getER else 1 / izq
            elif self.tipo == Operador.COSENO:
                return generador.addTrigonometrica(izq, 'Cos') if getER else math.cos(izq)
            elif self.tipo == Operador.SENO:
                return generador.addTrigonometrica(izq, 'Sen') if getER else math.sin(izq)
            elif self.tipo == Operador.TANGENTE:
                return generador.addTrigonometrica(izq, 'Tan') if getER else math.tan(izq)
            else:
                return 0


class Numero(Expression):

    def __init__(self, valor, fila, column):
        self.valor = valor
        super().__init__(fila, column)

    def ejecutar(self, getER):
        return self.valor


class Texto(Expression):

    def __init__(self, texto, linea, column):
        self.texto = texto
        self.linea = linea
        self.column = column

    def ejecutar(self, getER):
        return self.texto

class Estilo(Expression):

    def __init__(self, instruccion, color, tamanio, line, column):
        self.instruccion = instruccion
        self.color = color
        self.tamanio = tamanio
        self.line = line
        self.column = column

    def ejecutar(self, getER):
        return {self.instruccion, self.color, self.tamanio}


class Funcion(Expression):

    def __init__(self, titulo, descripcion, contenido, line, column):
        self.titulo = titulo
        self.descripcion = descripcion
        self.contenido = contenido
        self.line = line
        self.column = column

    def ejecutar(self, getER):
        return {self.titulo, self.descripcion, self.contenido}