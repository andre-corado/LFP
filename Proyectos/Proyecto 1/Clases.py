
class Error:
    def __init__(self, lexema, tipo, columna, fila):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna
        self.fila = fila

    def toString(self):
        return f"=======\nLexema: {self.lexema}\nTipo: {self.tipo}\nColumna: {self.columna}\nFila: {self.fila}\n======="
