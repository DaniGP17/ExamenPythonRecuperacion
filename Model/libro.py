from Model.articulo import Articulo
from Model.database import get_connection
from Model.prestable import Prestable


class Libro(Articulo, Prestable):
    def __init__(self, id: int, isbn : str, titulo, anio, f_adquisicion, prestado: bool, usuario_id, fecha_prestamo):
        Articulo.__init__(self, titulo, anio, f_adquisicion)
        Prestable.__init__(self, prestado, usuario_id, fecha_prestamo)

        self.id = id
        self.isbn = isbn

    @staticmethod
    def get_data() -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros")
        result = cursor.fetchall()
        conn.close()
        return result

    @staticmethod
    def get_by_id(id) -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM libros WHERE id = ?", (id,))
        result = cursor.fetchone()
        conn.close()
        return result

    @staticmethod
    def update_data(id, isbn, titulo, anio, f_adquisicion) -> None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE libros SET isbn = ?, titulo = ?, anio=?, fecha_adquisicion=? WHERE id = ?", (isbn, titulo, int(anio), f_adquisicion, int(id)))
        conn.commit()
        conn.close()

    @staticmethod
    def insert_data(isbn, titulo, anio, f_adquisicion) -> None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO libros (isbn, titulo, anio, fecha_adquisicion) VALUES (?, ?, ?, ?)", (isbn, titulo, int(anio), f_adquisicion))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_data(id) -> None:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM libros WHERE id = ?",(int(id),))
        conn.commit()
        conn.close()

    @staticmethod
    def get_csv_header() -> list:
        return ["id", "isbn", "titulo", "anio", "fecha_adquisicion", "prestado", "usuario_id", "fecha_prestamo"]

    def get_csv_data(self) -> list:
        return [self.id, self.isbn, self.titulo, self.anio, self.f_adquisicion, self.prestado, self.usuario_id, self.fecha_prestamo]

    def save_prestar(self) -> None:
        conn = get_connection()
        cursor = conn.cursor()
        print(f"SET PRESTADO: {self.prestado}")
        cursor.execute("UPDATE libros SET prestado = ?, numero_usuario=?, fecha_prestamo=? WHERE id = ?",(int(self.prestado), self.usuario_id, self.fecha_prestamo, self.id))
        conn.commit()
        conn.close()