import tkinter
from os.path import commonpath
from tkinter import ttk
import customtkinter as ctk


class PrestamoView(ctk.CTkToplevel):
    def __init__(self, controller, libro_id, submit_cb):
        super().__init__()
        self.__controller = controller
        self.__libro_id = libro_id
        self.__submit_cb = submit_cb
        self.initialize_window()
        self.create_ui()
        self.focus()
        self.mainloop()

    def initialize_window(self):
        self.title("PRESTAMO LIBRO")
        self.geometry("300x400")

    def create_ui(self):
        ctk.CTkLabel(self, text="BIBLIOTECA DGP", font=("Arial", 25)).pack(pady=5)

        ctk.CTkLabel(self, text="Prestado").pack(pady=5)
        prestado = tkinter.StringVar()
        tkinter.Entry(self, textvariable=prestado).pack(pady=3)

        ctk.CTkLabel(self, text="Numero Usuario").pack(pady=5)
        usuario_id = tkinter.StringVar()
        tkinter.Entry(self, textvariable=usuario_id).pack(pady=3)

        ctk.CTkLabel(self, text="Fecha Prestamo").pack(pady=5)
        fecha_prestamo = tkinter.StringVar()
        tkinter.Entry(self, textvariable=fecha_prestamo).pack(pady=3)

        ctk.CTkButton(self, text="Prestar", command=lambda: self.submit_data(self.__libro_id, prestado.get(), usuario_id.get(), fecha_prestamo.get())).pack(pady=20)

        libro = self.__controller.get_libro(self.__libro_id)
        prestado.set(libro.prestado)
        usuario_id.set(libro.usuario_id)
        fecha_prestamo.set(libro.fecha_prestamo)

    def submit_data(self, id, prestado, usuario_id, fecha_prestamo):
        try:
            self.__controller.prestar_libro(id, int(prestado), int(usuario_id), fecha_prestamo)
        except:
            print("Has introducido valores incorrectos para hacer el prestamo")
        self.__submit_cb()
        self.destroy()