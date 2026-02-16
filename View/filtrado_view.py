import tkinter
from os.path import commonpath
from tkinter import ttk
import customtkinter as ctk


class FiltradoView(ctk.CTkToplevel):
    def __init__(self, controller, submit_cb):
        super().__init__()
        self.__controller = controller
        self.__submit_cb = submit_cb
        self.initialize_window()
        self.create_ui()
        self.focus()
        self.mainloop()

    def initialize_window(self):
        self.title("FILTRAR LIBROS")
        self.geometry("300x400")

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

        ctk.CTkButton(self, text="Filtrar", command=lambda: self.filter_data(isbn.get(), titulo.get(), anio.get(), f_adquisicion.get())).pack(pady=20)

    def filter_data(self, isbn, titulo, anio, f_adquisicion):
        filters = {
            "isbn": isbn,
            "titulo": titulo,
            "anio": anio,
            "f_adquisicion": f_adquisicion
        }
        try:
            self.__controller.set_filtrado(filters)
        except:
            print("Has introducido valores incorrectos para hacer el filtrado")
        self.__submit_cb()
        self.destroy()