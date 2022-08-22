from curso import Curso


class Database:
    def __init__(self):
        self.cursos = []
        self.codigosCursos = []

    def cargaMasiva(self, ruta):
        archivo = open(ruta, 'r', encoding='utf8')
        lineas = archivo.readlines()
        print(lineas)
        for linea in lineas:
            fila = linea.split(',')
            curso = Curso(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
            self.agregarCurso(curso)
            print(fila)

    def agregarCurso(self, curso):
        if not (curso.codigo in self.codigosCursos):
            self.cursos.append(curso)
            self.codigosCursos.append(curso.codigo)
        else:
            cursoRegistrado = self.getCurso(curso.codigo)
            cursoRegistrado.sobreescribirCurso(curso.codigo, curso.nombre, curso.prerequisitos, curso.obligatorio,
                                               curso.semestre, curso.creditos, curso.estado)

    def getCurso(self, codigo):
        if codigo in self.codigosCursos:
            for curso in self.cursos:
                if curso.codigo == codigo:
                    return curso
        return None

    def eliminarCurso(self, codigo):
        if self.getCurso(codigo):
            curso = self.getCurso(codigo)
            self.cursos.remove(curso)
            self.codigosCursos.remove(codigo)
            return True
        else:
            return None

    def getCreditosAprobados(self):
        creditos = 0
        for curso in self.cursos:
            if curso.obligatorio and curso.estado == 0:
                creditos += curso.creditos
        return creditos

    def getCreditosCursando(self):
        creditos = 0
        for curso in self.cursos:
            if curso.estado == 1:
                creditos += curso.creditos
        return creditos

    def getCreditosPendientes(self):
        creditos = 0
        for curso in self.cursos:
            if curso.obligatorio and curso.estado == -1:
                creditos += curso.creditos
        return creditos

    def getCreditosHastaSemestreN(self, n):
        creditos = 0
        for curso in self.cursos:
            if curso.obligatorio and curso.semestre <= int(n):
                creditos += curso.creditos
        return creditos

    def getCreditosSemestre(self, n):
        creditos = [0, 0]  # [Aprobados, Pendientes]
        for curso in self.cursos:
            if curso.semestre == int(n):
                if curso.estado == 0:
                    creditos[0] += curso.creditos
                elif curso.estado == -1:
                    creditos[1] += curso.creditos
        return creditos


DB = Database()
