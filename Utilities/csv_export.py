import csv

from Model.libro import Libro


def write_libros(name, libros):
    with open(name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(Libro.get_csv_header())
        for i in libros:
            writer.writerow(i.get_csv_data())