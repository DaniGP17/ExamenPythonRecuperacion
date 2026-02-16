import tkinter
from os.path import commonpath
from tkinter import ttk
import customtkinter as ctk

from Utilities.utilidades import validate_isbn, format_title, format_year


class CreateModifyView(ctk.CTkToplevel):
    def __init__(self, controller, libro_id, submit_cb):
        super().__init__()
        self.__controller = controller
        self.__libro_id = libro_id
        self.__isCreate = libro_id is None
        self.__submit_cb = submit_cb
        self.initialize_window()
        self.create_ui()
        self.focus()
        self.mainloop()

    def initialize_window(self):
        self.title("CREAR / MODIFICAR LIBRO")
        self.geometry("300x450")

    def create_ui(self):
        ctk.CTkLabel(self, text="BIBLIOTECA DGP", font=("Arial", 25)).pack(pady=5)

        ctk.CTkLabel(self, text="ISBN").pack(pady=5)
        isbn = tkinter.StringVar()
        tkinter.Entry(self, textvariable=isbn).pack(pady=3)

        ctk.CTkLabel(self, text="Titulo").pack(pady=5)
        titulo = tkinter.StringVar()
        tkinter.Entry(self, textvariable=titulo).pack(pady=3)

        ctk.CTkLabel(self, text="Año").pack(pady=5)
        anio = tkinter.StringVar()
        tkinter.Entry(self, textvariable=anio).pack(pady=3)

        ctk.CTkLabel(self, text="Fecha Adquisicion").pack(pady=5)
        f_adquisicion = tkinter.StringVar()
        tkinter.Entry(self, textvariable=f_adquisicion).pack(pady=3)

        # Voy a comentar esto porque no tiene sentido editarlo manualmente, esto lo hará el otro boton de prestar
        '''ctk.CTkLabel(self, text="Prestado").pack(pady=5)
        prestado = tkinter.StringVar()
        tkinter.Entry(self, textvariable=prestado).pack(pady=3)

        ctk.CTkLabel(self, text="Numero Usuario").pack(pady=5)
        usuario_id = tkinter.StringVar()
        tkinter.Entry(self, textvariable=usuario_id).pack(pady=3)

        ctk.CTkLabel(self, text="Fecha Prestamo").pack(pady=5)
        fecha_prestamo = tkinter.StringVar()
        tkinter.Entry(self, textvariable=fecha_prestamo).pack(pady=3)'''

        ctk.CTkButton(self, text=("Crear" if self.__isCreate else "Actualizar"), command=lambda: self.submit_data(self.__libro_id, isbn.get(), titulo.get(), anio.get(), f_adquisicion.get())).pack(pady=20)

        if not self.__isCreate:
            libro = self.__controller.get_libro(self.__libro_id)
            isbn.set(libro.isbn)
            titulo.set(libro.titulo)
            anio.set(libro.anio)
            f_adquisicion.set(libro.f_adquisicion)
            '''prestado.set(libro.prestado)
            usuario_id.set(libro.usuario_id)
            fecha_prestamo.set(libro.fecha_prestamo)'''

    def submit_data(self, id, isbn, titulo, anio, f_adquisicion):
        if validate_isbn(isbn):
            titulo = format_title(titulo)
            anio = format_year(int(anio))
            if self.__isCreate:
                self.__controller.insert_libro(isbn, titulo, anio, f_adquisicion)
            else:
                self.__controller.update_libro(id, isbn, titulo, anio, f_adquisicion)
        else:
            print("El ISBN introducido es invalido")
        self.__submit_cb()
        self.destroy()