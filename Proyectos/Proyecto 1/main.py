import os
from pathlib import Path
import webbrowser
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import analizadorLexico


class Ventana:
    def __init__(self):
        self.editorTexto = None
        self.ventana = Tk()
        self.ventana.resizable(False, False)
        self.ventana.title('Proyecto 1 - LFP B+')
        self.Centrar(self.ventana, 1200, 800)
        self.ventana.geometry('1200x800')
        self.ventana.configure(bg='#3C3F41')
        self.Ventana()
        self.ventana.mainloop()

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho // 2)
        y = (altura_pantalla // 2) - (alto // 2)
        r.geometry(f'+{x}+{y}')

    def Ventana(self):
        self.ruta = None
        self.menu = Menu(self.ventana.master)
        self.ventana.config(menu=self.menu)
        self.menubar = Menu(self.menu, tearoff=0, bg='#cd8b62', activebackground='#475c6c')
        # Menú Archivo
        self.archivoMenu = Menu(self.menubar, tearoff=0, bg='#f7efd2', activebackground='#475c6c')
        self.archivoMenu.add_command(label="Abrir", font=("Roboto", 25), command=self.abrir)
        self.archivoMenu.add_command(label="Guardar", font=("Roboto", 25), command=self.guardar)
        self.archivoMenu.add_command(label="Guardar Como", font=("Roboto", 25), command=self.guardarComo)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Analizar", font=("Roboto", 25), command=self.analizar)
        self.archivoMenu.add_command(label="Errores", font=("Roboto", 25), command=self.errores)
        self.menubar.add_cascade(label="Archivo", menu=self.archivoMenu, font=("Roboto", 25))
        # Menú Ayuda
        self.ayudaMenu = Menu(self.menubar, tearoff=0, bg='#f7efd2', activebackground='#475c6c')
        self.ayudaMenu.add_command(label="Manual de Usuario", font=("Roboto", 25), command=self.manualDeUsuario)
        self.ayudaMenu.add_command(label="Manual Técnico", font=("Roboto", 25), command=self.manualTecnico)
        self.ayudaMenu.add_separator()
        self.ayudaMenu.add_command(label="Temas de Ayuda", font=("Roboto", 25), command=self.infoAutor)
        self.menubar.add_cascade(label="Ayuda", menu=self.ayudaMenu, font=("Roboto", 25))
        self.menubar.add_separator()
        self.menubar.add_command(label="Salir", command=quit, font=("Roboto", 25))
        self.menu.add_cascade(label="Menu", menu=self.menubar)
        # Editor de Texto
        self.editorTexto = Text(self.ventana, font=('Fira Mono Regular', 14), width=90, height=25, borderwidth=10,
                                fg='#A9B7C6', bg="#2B2B2B")
        self.editorTexto.place(x=100, y=150)
        # Label con Nombre del Archivo dentro del Editor de Texto
        self.nombreArchivo = Label(font=('Roboto', 20), width=73, bg='#4D4D4D', fg='#A9B7C6')
        self.nombreArchivo.config(text='ARCHIVO SIN NOMBRE')
        self.nombreArchivo.place(x=50, y=50)

    def abrir(self):
        ruta = filedialog.askopenfilename(initialdir="C:/Users/SergioLima/Downloads",
                                          title="Selecciona un archivo:",
                                          filetypes=(("TXT files", "*.txt*"), ("All files", "*.*")), )
        self.ruta = ruta
        try:
            f = open(ruta, 'rt')
            text = f.read()
            self.editorTexto.delete('1.0', END)
            self.editorTexto.insert('1.0', text)
            f.close()
            self.ruta = ruta
            ruta_dividida = ruta.split('/')
            self.nombreArchivo.config(text=ruta_dividida[-1])
        except:
            tkinter.messagebox.showerror(message="No pudo leerse el archivo", title='ERROR')

    def guardar(self):
        ruta = self.ruta
        text = self.editorTexto.get('1.0', END)
        # Si el archivo es nuevo
        if ruta is None:
            self.guardarComo()
        else:
            try:
                with open(ruta, "w") as f:
                    f.write(text)
                    f.close()
                    self.ruta = ruta
                    ruta_dividida = ruta.split('/')
                    self.nombreArchivo.config(text=ruta_dividida[-1])

            except FileNotFoundError:
                tkinter.messagebox.showerror(message="No pudo leerse el archivo", title='ERROR')

    def guardarComo(self):
        text = self.editorTexto.get('1.0', END)
        ruta = filedialog.asksaveasfilename(
            filetypes=[("txt file", ".txt")], defaultextension=".txt")
        f = open(ruta, 'w')
        f.write(text)
        f.close()
        self.ruta = ruta
        ruta_dividida = ruta.split('/')
        self.nombreArchivo.config(text=ruta_dividida[-1])

    def manualDeUsuario(self):
        webbrowser.open_new('Manual De Usuario.pdf')

    def manualTecnico(self):
        webbrowser.open_new('Manual Tecnico.pdf')

    def infoAutor(self):
        tkinter.messagebox.showinfo('Información del Estudiante',
                                    'Nombre:\nSergio André Lima Corado\n\nCarné:\n\t202100154\n'
                                    'Sección:\n\tB+')

    def analizar(self):
        analizadorLexico.analizar(self.editorTexto.get('1.0', END))
        ruta = Path().absolute()
        webbrowser.open_new('file://' + str(ruta) + '/RESULTADOS_202100154.html')


    def errores(self):
        ruta = Path().absolute()
        webbrowser.open_new('file://' + str(ruta) + '/ERRORES_202100154.html')

if __name__ == '__main__':
    Ventana()
