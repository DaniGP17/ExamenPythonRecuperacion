from abc import ABC, abstractmethod
from Utilities.utilidades import format_title, format_year

class Articulo(ABC):
    def __init__(self, titulo, anio, f_adquisicion):
        self.titulo = format_title(titulo)
        self.anio = format_year(anio)
        self.f_adquisicion = f_adquisicion