from models.libros import Libros
from database import db, logger

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
        for l in Libros.select():
            
            if l.id_editorial:
                editorial = l.id_editorial.nombre
            else:
                editorial = "Sin editorial"

            if l.id_genero:
                genero = l.id_genero.nombre
            else:
                genero = "Sin genero"
            
            if l.id_autor:
                autor = l.id_autor.nombre
            else:
                autor = "Sin autor"

            logger.info(f"titulo={l.titulo}, n_paginas={l.n_paginas}, editorial={editorial}, genero={genero}, autor={autor}")