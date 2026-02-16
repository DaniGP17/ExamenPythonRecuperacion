from Model.libro import Libro


class ControladorLibros():
    def __init__(self):
        self.filters = {
            "isbn": "",
            "titulo": "",
            "anio": "",
            "f_adquisicion": ""
        }

    @staticmethod
    def validate_filter(excepted, value):
        if str(excepted) == "":
            return True
        return str(excepted) in str(value)

    def get_libros(self):
        data = Libro.get_data()
        result = []
        for i in data:
            if not ControladorLibros.validate_filter(self.filters['isbn'], i[1]):
                continue
            if not ControladorLibros.validate_filter(self.filters['titulo'], i[2]):
                continue
            if not ControladorLibros.validate_filter(self.filters['anio'], i[3]):
                continue
            if not ControladorLibros.validate_filter(self.filters['f_adquisicion'], i[4]):
                continue
            result.append(Libro(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        return result

    def get_libro(self, id):
        raw_data = Libro.get_by_id(id)
        return Libro(raw_data[0], raw_data[1], raw_data[2], raw_data[3], raw_data[4], raw_data[5], raw_data[6], raw_data[7])

    def update_libro(self, id, isbn, titulo, anio, f_adquisicion):
        Libro.update_data(id, isbn, titulo, anio, f_adquisicion)

    def insert_libro(self, isbn, titulo, anio, f_adquisicion):
        Libro.insert_data(isbn, titulo, anio, f_adquisicion)

    def delete_libro(self, id):
        Libro.delete_data(id)

    def get_expirated(self):
        libros = self.get_libros()
        results = []
        for libro in libros:
            if not libro.validate_time():
                results.append(libro)
        return results

    def prestar_libro(self, id, prestado, usuario_id, fecha_prestamo):
        libro = self.get_libro(id)
        if prestado:
            libro.prestar(usuario_id, fecha_prestamo)
        else:
            libro.desprestar()
        libro.save_prestar()

    def set_filtrado(self, filters):
        self.filters = filters