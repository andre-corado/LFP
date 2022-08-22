class Curso:
    def __init__(self, codigo, nombre, prerequisitos, opcionalidad, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerequisitos = prerequisitos.split(';')
        if opcionalidad == '1':
            self.obligatorio = True
        else:
            self.obligatorio = False
        self.semestre = int(semestre)
        self.creditos = int(creditos)
        self.estado = int(estado)

    def editarCurso(self, codigo, nombre, prerequisitos, opcionalidad, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerequisitos = prerequisitos.split(';')
        if opcionalidad == '1':
            self.obligatorio = True
        else:
            self.obligatorio = False
        self.semestre = int(semestre)
        self.creditos = int(creditos)
        self.estado = int(estado)

    def sobreescribirCurso(self, codigo, nombre, prerequisitos, opcionalidad, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerequisitos = prerequisitos
        self.opcionalidad = opcionalidad
        self.semestre = int(semestre)
        self.creditos = int(creditos)
        self.estado = int(estado)

    def printObligatorio(self):
        if self.obligatorio:
            return 'Obligatorio'
        else:
            return 'Opcional'

    def printEstado(self):
        if self.estado == 0:
            return 'Aprobado'
        elif self.estado == 1:
            return 'Cursando'
        else:
            return 'Pendiente'

    def printPreRequisitos(self):
        if self.prerequisitos is None:
            return 'Ninguno'
        else:
            txt = ", ".join(self.prerequisitos)
            return txt
