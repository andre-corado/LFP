import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from database import DB
from curso import Curso

''' Paleta de colores:
191935 Azul Oscuro
2D4263 Azul Claro
C84B31 Rojo
ECDBBA Amarillo Pálido
EEEEEE Blanco
'''


class PantallaPrincipal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Práctica 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#191935')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=700, width=1100)
        self.frame.config(bg='#2D4263')
        self.frame.pack(padx=0, pady=50)
        Label(self.frame, text="Curso: Lenguajes Formales y de Programación\n"
                               "Nombre: Sergio André Lima Corado\nCarné: 202100154",
              font=('Roboto', 35), fg='#EEEEEE', bg='#C84B31',
              width=40).place(x=5, y=50)
        Button(self.frame, text="Cargar Archivo", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.IrCargarArchivos).place(x=350, y=300)
        Button(self.frame, text="Gestionar Cursos", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.IrGestionarCursos).place(x=350, y=400)
        Button(self.frame, text="Conteo de Créditos", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.IrCreditos).place(x=350, y=500)
        Button(self.frame, text="Salir", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.Salir).place(x=350, y=600)
        self.frame.mainloop()

    def IrCargarArchivos(self):
        self.ventana.destroy()
        PantallaCargarArchivos()

    def IrCreditos(self):
        self.ventana.destroy()
        PantallaCreditos()

    def IrGestionarCursos(self):
        self.ventana.destroy()
        PantallaGestionarCursos()

    def Salir(self):
        self.ventana.destroy()


class PantallaCargarArchivos:
    def __init__(self):
        self.entry = None
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Práctica 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#191935')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=700, width=1100)
        self.frame.config(bg='#2D4263')
        self.frame.pack(padx=0, pady=50)
        Label(self.frame, text="Cargar Archivo",
              font=('Roboto', 40), fg='#EEEEEE', bg='#C84B31',
              width=37).place(x=0, y=0)
        Label(self.frame, text="Ruta:",
              font=('Roboto', 40), fg='#EEEEEE', bg='#2D4263',
              width=10).place(x=50, y=225)
        Button(self.frame, text="Regresar", font=('Roboto', 20), fg='#000000',
               bg='#EEEEEE', width=8, command=self.Regresar).place(x=950, y=75)
        Button(self.frame, text="Examinar", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=10, command=self.AbrirFileExplorer).place(x=800, y=300)
        Button(self.frame, text="Cargar", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.CargarArchivo).place(x=350, y=550)
        self.entry = tkinter.Entry(width=40, font=('Roboto', 20))
        self.entry.place(x=175, y=375)
        self.frame.mainloop()

    def Regresar(self):
        self.ventana.destroy()
        PantallaPrincipal()

    def CargarArchivo(self):
        ruta = self.entry.get()
        DB.cargaMasiva(ruta)
        messagebox.showinfo(message='Todos los cursos fueron agregados exitosamente.', title='CURSOS AGREGADOS')
        self.ventana.destroy()
        PantallaPrincipal()

    def AbrirFileExplorer(self):
        ruta = filedialog.askopenfilename(initialdir="C:/Users/SergioLima/Downloads", title="Select a File",
                                          filetypes=(("LFP files", "*.lfp*"),
                                                     ("CSV files", "*.csv*"),
                                                     ("All files", "*.*")),
                                          )
        self.entry.delete(0, END)
        self.entry.insert(0, ruta)


class PantallaGestionarCursos:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Práctica 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#191935')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=700, width=1100)
        self.frame.config(bg='#2D4263')
        self.frame.pack(padx=0, pady=50)
        Label(self.frame, text="Gestionar Cursos",
              font=('Roboto', 40), fg='#EEEEEE', bg='#C84B31',
              width=37).place(x=0, y=0)
        Button(self.frame, text="Regresar", font=('Roboto', 20), fg='#000000',
               bg='#EEEEEE', width=8, command=self.Regresar).place(x=950, y=75)

        Button(self.frame, text="Listar Cursos", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.IrListarCursos).place(x=350, y=200)
        Button(self.frame, text="Agregar Curso", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.IrAgregarCurso).place(x=350, y=300)
        Button(self.frame, text="Editar Curso", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.IrEditarCurso).place(x=350, y=400)
        Button(self.frame, text="Eliminar Curso", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.IrEliminarCurso).place(x=350, y=500)
        self.frame.mainloop()

    def IrListarCursos(self):
        self.ventana.destroy()
        PantallaListarCursos()

    def IrAgregarCurso(self):
        self.ventana.destroy()
        PantallaAgregarCurso()

    def IrEditarCurso(self):
        self.ventana.destroy()
        PantallaEditarCurso()

    def IrEliminarCurso(self):
        self.ventana.destroy()
        PantallaEliminarCurso()

    def Regresar(self):
        self.ventana.destroy()
        PantallaPrincipal()


class PantallaAgregarCurso:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Práctica 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#191935')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=700, width=1100)
        self.frame.config(bg='#2D4263')
        self.frame.pack(padx=0, pady=50)
        Label(self.frame, text="Agregar Curso",
              font=('Roboto', 40), fg='#EEEEEE', bg='#C84B31',
              width=37).place(x=0, y=0)
        Button(self.frame, text="Regresar", font=('Roboto', 20), fg='#000000',
               bg='#EEEEEE', width=8, command=self.Regresar).place(x=950, y=75)

        Label(self.frame, text="Código",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=100)
        Label(self.frame, text="Nombre",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=200)
        Label(self.frame, text="Pre-Requisito",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=300)
        Label(self.frame, text="Semestre",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=400)
        Label(self.frame, text="Créditos",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=500)
        Label(self.frame, text="Opcionalidad",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=500, y=400)
        Label(self.frame, text="Estado",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=500, y=500)

        Button(self.frame, text="Agregar Curso", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.AgregarCurso).place(x=650, y=600)

        self.codigotxt = tkinter.Entry(width=20, font=('Roboto', 20), justify='center')
        self.codigotxt.place(x=325, y=150)
        self.nombretxt = tkinter.Entry(width=40, font=('Roboto', 20), justify='center')
        self.nombretxt.place(x=325, y=250)
        self.prerequisitotxt = tkinter.Entry(width=20, font=('Roboto', 20), justify='center')
        self.prerequisitotxt.place(x=325, y=350)

        self.semestreCombo = ttk.Combobox(self.ventana, values=['1', '2', '3', '4', '5',
                                                                '6', '7', '8', '9', '10'],
                                          font=('Roboto', 20), width=5, state='readonly',
                                          justify='center')
        self.semestreCombo.current(0)
        self.semestreCombo.place(x=325, y=450)
        self.creditosCombo = ttk.Combobox(self.ventana, values=['0', '1', '2', '3', '4', '5',
                                                                '6', '7', '8', '9', '10'],
                                          font=('Roboto', 20), width=5, state='readonly',
                                          justify='center')
        self.creditosCombo.current(0)
        self.creditosCombo.place(x=325, y=550)
        self.opcionalidadCombo = ttk.Combobox(self.ventana, values=['Obligatorio', 'Opcional'],
                                              font=('Roboto', 20), width=10, state='readonly',
                                              justify='center')
        self.opcionalidadCombo.current(0)
        self.opcionalidadCombo.place(x=750, y=450)
        self.estadoCombo = ttk.Combobox(self.ventana, values=['Aprobado', 'Cursando', 'Pendiente'],
                                        font=('Roboto', 20), width=10, state='readonly',
                                        justify='center')
        self.estadoCombo.current(0)
        self.estadoCombo.place(x=750, y=550)

        self.frame.mainloop()

    def Regresar(self):
        self.ventana.destroy()
        PantallaGestionarCursos()

    def AgregarCurso(self):
        if (not self.nombretxt.get() == '') and (not self.codigotxt.get() == '')\
                and (not self.prerequisitotxt.get() == ''):
            curso = Curso(self.codigotxt.get(), self.nombretxt.get(), self.prerequisitotxt.get(),
                          self.getOpcionalidad(), self.semestreCombo.get(), self.creditosCombo.get(),
                          self.getEstado())
            DB.agregarCurso(curso)
            messagebox.showinfo(message='El curso fue agregado exitosamente.', title='CURSO AGREGADO')
            self.ventana.destroy()
            PantallaPrincipal()
        else:
            messagebox.showerror(message='Debe de llenar todos los campos', title='ERROR')

    def getOpcionalidad(self):
        if self.opcionalidadCombo.get() == 'Obligatorio':
            return '1'
        else:
            return '0'

    def getEstado(self):
        if self.estadoCombo.get() == 'Aprobado':
            return '0'
        elif self.estadoCombo.get() == 'Cursando':
            return '1'
        else:
            return '-1'


class PantallaEditarCurso:
    def __init__(self):
        self.curso = None
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Práctica 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#191935')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=700, width=1100)
        self.frame.config(bg='#2D4263')
        self.frame.pack(padx=0, pady=50)
        Label(self.frame, text="Editar Curso",
              font=('Roboto', 40), fg='#EEEEEE', bg='#C84B31',
              width=37).place(x=0, y=0)
        Button(self.frame, text="Regresar", font=('Roboto', 20), fg='#000000',
               bg='#EEEEEE', width=8, command=self.Regresar).place(x=950, y=75)

        Label(self.frame, text="Código",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=100)
        Label(self.frame, text="Nombre",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=200)
        Label(self.frame, text="Pre-Requisito",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=300)
        Label(self.frame, text="Semestre",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=400)
        Label(self.frame, text="Créditos",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=50, y=500)
        Label(self.frame, text="Opcionalidad",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=500, y=400)
        Label(self.frame, text="Estado",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=0).place(x=500, y=500)

        self.mostrarbtn = Button(self.frame, text="Mostrar", font=('Roboto', 15), fg='#EEEEEE',
               bg='#C84B31', width=8, command=self.mostrarCurso)
        self.mostrarbtn.place(x=625, y=99)
        Button(self.frame, text="Editar Curso", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.editarCurso).place(x=650, y=600)

        self.codigotxt = tkinter.Entry(width=20, font=('Roboto', 20), justify='center')
        self.codigotxt.place(x=325, y=150)
        self.nombretxt = tkinter.Entry(width=40, font=('Roboto', 20), justify='center', state='disabled')
        self.nombretxt.place(x=325, y=250)
        self.prerequisitotxt = tkinter.Entry(width=20, font=('Roboto', 20), justify='center', state='disabled')
        self.prerequisitotxt.place(x=325, y=350)

        self.semestreCombo = ttk.Combobox(self.ventana, values=['1', '2', '3', '4', '5',
                                                                '6', '7', '8', '9', '10'],
                                          font=('Roboto', 20), width=5, state='readonly',
                                          justify='center')
        self.semestreCombo.configure(state='disabled')
        self.semestreCombo.place(x=325, y=450)
        self.creditosCombo = ttk.Combobox(self.ventana, values=['0', '1', '2', '3', '4', '5',
                                                                '6', '7', '8', '9', '10'],
                                          font=('Roboto', 20), width=5, state='readonly',
                                          justify='center')
        self.creditosCombo.configure(state='disabled')
        self.creditosCombo.place(x=325, y=550)
        self.opcionalidadCombo = ttk.Combobox(self.ventana, values=['Obligatorio', 'Opcional'],
                                              font=('Roboto', 20), width=10, state='readonly',
                                              justify='center')
        self.opcionalidadCombo.configure(state='disabled')
        self.opcionalidadCombo.place(x=750, y=450)
        self.estadoCombo = ttk.Combobox(self.ventana, values=['Aprobado', 'Cursando', 'Pendiente'],
                                        font=('Roboto', 20), width=10, state='readonly',
                                        justify='center')
        self.estadoCombo.configure(state='disabled')
        self.estadoCombo.place(x=750, y=550)

        self.frame.mainloop()

    def Regresar(self):
        self.ventana.destroy()
        PantallaGestionarCursos()

    def mostrarCurso(self):
        if DB.getCurso(self.codigotxt.get()):
            self.curso = DB.getCurso(self.codigotxt.get())

            self.mostrarbtn.configure(state='disabled')
            self.nombretxt.configure(state='normal')
            self.prerequisitotxt.configure(state='normal')
            self.opcionalidadCombo.configure(state='readonly')
            self.creditosCombo.configure(state='readonly')
            self.semestreCombo.configure(state='readonly')
            self.estadoCombo.configure(state='readonly')

            self.nombretxt.insert(0, self.curso.nombre)
            self.prerequisitotxt.insert(0, ';'.join(self.curso.prerequisitos))
            self.opcionalidadCombo.set(self.curso.printObligatorio())
            self.creditosCombo.set(self.curso.creditos)
            self.semestreCombo.set(self.curso.semestre)
            self.estadoCombo.set(self.curso.printEstado())
        else:
            messagebox.showerror(message='El código ingresado no pertenece a ningún curso.', title='ERROR')

    def editarCurso(self):
        if DB.getCurso(self.codigotxt.get()):
            if (not self.nombretxt.get() == '') and (not self.codigotxt.get() == ''):
                self.curso.editarCurso(self.codigotxt.get(), self.nombretxt.get(), self.prerequisitotxt.get(),
                                       self.getOpcionalidad(), self.semestreCombo.get(), self.creditosCombo.get(),
                                       self.getEstado())
                messagebox.showinfo(message='El curso ha sido editado exitosamente.', title='CURSO EDITADO')
                self.ventana.destroy()
                PantallaPrincipal()
            else:
                messagebox.showerror(message='Debe de llenar todos los campos', title='ERROR')
        else:
            messagebox.showerror(message='El código ingresado no pertenece a ningún curso.', title='ERROR')

    def getOpcionalidad(self):
        if self.opcionalidadCombo.get() == 'Obligatorio':
            return '1'
        else:
            return '0'

    def getEstado(self):
        if self.estadoCombo.get() == 'Aprobado':
            return '0'
        elif self.estadoCombo.get() == 'Cursando':
            return '1'
        else:
            return '-1'


class PantallaCreditos:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Práctica 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#191935')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=700, width=1100)
        self.frame.config(bg='#2D4263')
        self.frame.pack(padx=0, pady=50)
        Label(self.frame, text="Conteo de Créditos",
              font=('Roboto', 40), fg='#EEEEEE', bg='#C84B31',
              width=37).place(x=0, y=0)
        Button(self.frame, text="Regresar", font=('Roboto', 20), fg='#000000',
               bg='#EEEEEE', width=8, command=self.Regresar).place(x=950, y=75)

        Label(self.frame, text="Cambio Calificación 1:",
              font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
              width=15).place(x=25, y=150)
        self.aprobadostxt = Label(self.frame, text=DB.getCreditosAprobados(),
                                  font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
                                  width=5)
        self.aprobadostxt.place(x=350, y=150)
        Label(self.frame, text="Créditos Cursando:",
              font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
              width=15).place(x=550, y=150)
        self.cursandotxt = Label(self.frame, text=DB.getCreditosCursando(),
                                 font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
                                 width=5)
        self.cursandotxt.place(x=875, y=150)
        Label(self.frame, text="Créditos Pendientes:",
              font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
              width=16).place(x=20, y=250)
        self.pendientestxt = Label(self.frame, text=DB.getCreditosPendientes(),
                                   font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
                                   width=5)
        self.pendientestxt.place(x=350, y=250)
        Label(self.frame, text="Créditos Obligatorios hasta semestre N:",
              font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
              width=30).place(x=170, y=350)
        self.hastaSemestreNtxt = Label(self.frame, text="XXX",
                                       font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
                                       width=5)
        self.hastaSemestreNtxt.place(x=750, y=350)
        Label(self.frame, text="Créditos del Semestre:",
              font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
              width=18).place(x=50, y=525)
        Label(self.frame, text="Aprobados:",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=18).place(x=600, y=525)
        Label(self.frame, text="Pendientes:",
              font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
              width=18).place(x=600, y=625)
        self.delSemestretxt = Label(self.frame, text="XXX",
                                    font=('Roboto', 25), fg='#EEEEEE', bg='#2D4263',
                                    width=5)
        self.delSemestretxt.place(x=400, y=525)
        self.delSemestreAprobadostxt = Label(self.frame, text="XXX",
                                    font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
                                    width=5)
        self.delSemestreAprobadostxt.place(x=850, y=525)
        self.delSemestrePendientestxt = Label(self.frame, text="XXX",
                                             font=('Roboto', 20), fg='#EEEEEE', bg='#2D4263',
                                             width=5)
        self.delSemestrePendientestxt.place(x=850, y=625)

        self.comboSemestre1 = ttk.Combobox(self.ventana, values=['1', '2', '3', '4', '5',
                                                                 '6', '7', '8', '9', '10'],
                                           font=('Roboto', 33), width=5, state='readonly',
                                           justify='center')
        self.comboSemestre1.place(x=450, y=475)
        self.comboSemestre2 = ttk.Combobox(self.ventana, values=['1', '2', '3', '4', '5',
                                                                 '6', '7', '8', '9', '10'],
                                           font=('Roboto', 33), width=5, state='readonly',
                                           justify='center')
        self.comboSemestre2.place(x=200, y=650)

        Button(self.frame, text="Contar", font=('Roboto', 20), fg='#000000',
               bg='#ECDBBA', width=8, command=self.contarCreditosHastaSemestreN).place(x=550, y=425)
        Button(self.frame, text="Contar", font=('Roboto', 20), fg='#000000',
               bg='#ECDBBA', width=8, command=self.contarCreditosSemestre).place(x=300, y=600)
        self.frame.mainloop()

    def Regresar(self):
        self.ventana.destroy()
        PantallaPrincipal()

    def contarCreditosHastaSemestreN(self):
        txt = DB.getCreditosHastaSemestreN(self.comboSemestre1.get())
        self.hastaSemestreNtxt.config(text=txt)

    def contarCreditosSemestre(self):
        creditos = DB.getCreditosSemestre(self.comboSemestre2.get())
        self.delSemestretxt.config(text=str(creditos[0]+creditos[1]))
        self.delSemestreAprobadostxt.config(text=str(creditos[0]))
        self.delSemestrePendientestxt.config(text=str(creditos[1]))


class PantallaEliminarCurso:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Práctica 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#191935')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=700, width=1100)
        self.frame.config(bg='#2D4263')
        self.frame.pack(padx=0, pady=50)
        Label(self.frame, text="Eliminar Curso",
              font=('Roboto', 40), fg='#EEEEEE', bg='#C84B31',
              width=37).place(x=0, y=0)
        Label(self.frame, text="Código del Curso:",
              font=('Roboto', 40), fg='#EEEEEE', bg='#2D4263',
              width=15).place(x=50, y=225)
        Button(self.frame, text="Regresar", font=('Roboto', 20), fg='#000000',
               bg='#EEEEEE', width=8, command=self.Regresar).place(x=950, y=75)
        Button(self.frame, text="Eliminar", font=('Roboto', 25), fg='#000000',
               bg='#ECDBBA', width=20, command=self.eliminarCurso).place(x=650, y=525)
        self.entry = tkinter.Entry(width=20, font=('Roboto', 40), justify='center')
        self.entry.place(x=100, y=400)
        self.frame.mainloop()

    def Regresar(self):
        self.ventana.destroy()
        PantallaGestionarCursos()

    def eliminarCurso(self):
        if DB.eliminarCurso(self.entry.get()):
            messagebox.showinfo(message='Curso eliminado correctamente.', title='ELIMINADO')
            self.ventana.destroy()
            PantallaPrincipal()
        else:
            messagebox.showerror(message='El código ingresado no pertenece a ningún curso.', title='ERROR')


class PantallaListarCursos():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Práctica 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#191935')
        self.Ventana()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()

        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.frame = Frame(height=700, width=1100)
        self.frame.config(bg='#2D4263')
        self.frame.pack(padx=0, pady=50)
        Label(self.frame, text="Listar Cursos",
              font=('Roboto', 40), fg='#EEEEEE', bg='#C84B31',
              width=37).place(x=0, y=0)
        Button(self.frame, text="Regresar", font=('Roboto', 20), fg='#000000',
               bg='#EEEEEE', width=8, command=self.Regresar).place(x=950, y=75)

        tabla = ttk.Treeview(self.frame, columns=('#0', '#1', '#2', '#3', '#4', '#5'), height=14, selectmode='browse')

        style = ttk.Style()
        style.configure(
            'Treeview',
            background='silver',
            foreground='black',
            rowheight=25,
            fielbackground='silver'
        )
        style.map(
            'Treeview',
            background=[('selected', 'green')]
        )

        tabla.grid(row=0, column=0, columnspan=2)
        tabla.column('#0', width=100, anchor=CENTER)
        tabla.column('#1', width=225, anchor=CENTER)
        tabla.column('#2', width=150, anchor=CENTER)
        tabla.column('#3', width=150, anchor=CENTER)
        tabla.column('#4', width=100, anchor=CENTER)
        tabla.column('#5', width=100, anchor=CENTER)
        tabla.column('#6', width=100, anchor=CENTER)

        tabla.heading("#0", text='Código', anchor=CENTER)
        tabla.heading("#1", text='Nombre', anchor=CENTER)
        tabla.heading('#2', text='Pre-Requisitos', anchor=CENTER)
        tabla.heading('#3', text='Opcionalidad', anchor=CENTER)
        tabla.heading('#4', text='Semestre', anchor=CENTER)
        tabla.heading('#5', text='Créditos', anchor=CENTER)
        tabla.heading('#6', text='Estado', anchor=CENTER)

        for curso in DB.cursos:
            tabla.insert("", END, text=curso.codigo,
                         values=(curso.nombre, curso.printPreRequisitos(), curso.printObligatorio(),
                                 curso.semestre, curso.creditos, curso.printEstado()))
        tabla.place(x=85, y=150)
        self.frame.mainloop()

    def Regresar(self):
        self.ventana.destroy()
        PantallaGestionarCursos()
