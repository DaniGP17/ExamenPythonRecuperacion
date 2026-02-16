from abc import ABC, abstractmethod
from datetime import date


class Prestable(ABC):
    num_dias = 31
    def __init__(self, prestado: bool, usuario_id, fecha_prestamo):
        self.prestado = prestado
        self.usuario_id = usuario_id
        self.fecha_prestamo = fecha_prestamo

    def validate_time(self) -> bool:
        if self.fecha_prestamo is None:
            return True
        today = date.today()
        data = self.fecha_prestamo.split('-')
        formated_date: date = date(int(data[0]), int(data[1]), int(data[2]))
        diff = abs((today - formated_date).days)
        return diff <= self.num_dias

    def prestar(self, usuario_id, fecha_prestamo):
        self.prestado = 1
        self.usuario_id = usuario_id
        self.fecha_prestamo = fecha_prestamo

    def desprestar(self):
        self.prestado = 0
        self.usuario_id = None
        self.fecha_prestamo = None