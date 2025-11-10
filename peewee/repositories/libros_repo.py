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

    @staticmethod
    def actualizar_libro(antiguo, nuevo):
        query = Libros.update(titulo = nuevo).where(Libros.titulo == antiguo)
        query.execute()

    @staticmethod
    def eliminar_libro(nombre):
        try:
            libro = Libros.get(Libros.titulo == nombre)
            libro.delete_instance() # tambien se puede hacer Libros.delete_instance(autor)
            logger.info("Libro borrado correctamente")
        except Libros.DoesNotExist:
            logger.info("No se ha encontrado ningun libro con ese nombre")