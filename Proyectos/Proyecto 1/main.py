from tkinter import *
from tkinter import filedialog


class Ventana:
    def __init__(self):
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
        self.menu = Menu(self.ventana.master)
        self.ventana.config(menu=self.menu)
        self.menubar = Menu(self.menu, tearoff=0, bg='#cd8b62', activebackground='#475c6c')
        # Menú Archivo
        self.archivoMenu = Menu(self.menubar, tearoff=0, bg='#f7efd2', activebackground='#475c6c')
        self.archivoMenu.add_command(label="Abrir", font=("Roboto", 25), command=self.abrir)
        self.archivoMenu.add_command(label="Guardar", font=("Roboto", 25))
        self.archivoMenu.add_command(label="Guardar Como", font=("Roboto", 25))
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Analizar", font=("Roboto", 25))
        self.archivoMenu.add_command(label="Errores", font=("Roboto", 25))
        self.menubar.add_cascade(label="Archivo", menu=self.archivoMenu, font=("Roboto", 25))
        # Menú Ayuda
        self.ayudaMenu = Menu(self.menubar, tearoff=0, bg='#f7efd2', activebackground='#475c6c')
        self.ayudaMenu.add_command(label="Manual de Usuario", font=("Roboto", 25))
        self.ayudaMenu.add_command(label="Manual Técnico", font=("Roboto", 25))
        self.ayudaMenu.add_separator()
        self.ayudaMenu.add_command(label="Temas de Ayuda", font=("Roboto", 25))
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
                                          filetypes=(("LFP files", "*.lfp*"), ("All files", "*.*")), )


if __name__ == '__main__':
    Ventana()