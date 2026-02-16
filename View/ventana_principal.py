import tkinter
from tkinter import ttk
import customtkinter as ctk

from Controller.controlador_libros import ControladorLibros
from Utilities.csv_export import write_libros
from View.create_modify_view import CreateModifyView
from View.filtrado_view import FiltradoView
from View.prestamo_view import PrestamoView


def selection(org_fun):
    def intern_cb(*args, **kwargs):
        self = args[0]
        sel = self.get_selected()
        if sel is None:
            return print("Tienes que tener algo seleccionado")
        return org_fun(self, sel)
    return intern_cb

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controller = ControladorLibros()
        self.initialize_window()
        self.tree = None
        self.create_ui()
        self.load_data()

    def initialize_window(self):
        self.title("BIBLIOTECA")
        self.geometry("1600x500")

    def create_ui(self):
        ctk.CTkLabel(self, text="BIBLIOTECA DGP", font=("Arial", 25)).pack(pady=5)

        ctk.CTkButton(self, text="Filtrar", command=self.abrir_filtrado).pack(pady=5)

        cabecera = ["ISBN", "Titulo", "Año", "Fecha Adquisicion", "Prestado", "Num Usuario", "Fecha Prestamo"]
        self.tree = ttk.Treeview(self, height=12, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7'))
        for i in range(0, len(cabecera)):
            self.tree.heading(f'#{i}', text=cabecera[i], anchor=tkinter.CENTER)
        self.tree.pack(padx=20)

        ctk.CTkButton(self, text="Prestar Libro", command=self.prestar_libro).pack(pady=5)
        ctk.CTkButton(self, text="Crear Libro", command=self.crear_libro).pack(pady=5)
        ctk.CTkButton(self, text="Eliminar Libro", command=self.eliminar_libro).pack(pady=5)
        ctk.CTkButton(self, text="Editar Libro", command=self.editar_libro).pack(pady=5)
        ctk.CTkButton(self, text="Exportar CSV", command=self.exportar_csv).pack(pady=5)

    def get_selected(self):
        selection = self.tree.selection()
        if len(selection) < 1:
            return None
        return selection[0]

    def load_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for i in self.controller.get_libros():
            self.tree.insert("", 0, iid=i.id, text=i.isbn, values=(i.titulo, i.anio, i.f_adquisicion, i.prestado, i.usuario_id, i.fecha_prestamo))

    @selection
    def prestar_libro(self, id : int):
        PrestamoView(self.controller, id, self.load_data)

    def crear_libro(self):
        CreateModifyView(self.controller, None, self.load_data)

    @selection
    def editar_libro(self, id : int):
        CreateModifyView(self.controller, id, self.load_data)

    @selection
    def eliminar_libro(self, id: int):
        self.controller.delete_libro(id)
        self.load_data()

    def exportar_csv(self):
        expired = self.controller.get_expirated()
        write_libros("expirated_libros.csv", expired)

    def abrir_filtrado(self):
        FiltradoView(self.controller, self.load_data)