from models.libros import Libros
from database import db

class LibrosRepository:
    @staticmethod
    def create_libros(titulo, n_paginas, id_editorial, id_genero, id_autor):
        return Libros.create(
            titulo = titulo,
            n_paginas = n_paginas,
            id_editorial = id_editorial,
            id_genero = id_genero,
            id_autor = id_autor
        )

    @staticmethod
    def ingesta_multiple(lista_tuplas):
        with db.atomic():
            Libros.insert_many(lista_tuplas, fields=[
                Libros.titulo,
                Libros.n_paginas,
                Libros.id_editorial,
                Libros.id_genero,
                Libros.id_autor
            ]).execute()

    @staticmethod
    def consulta_todos():
        return Libros.select()