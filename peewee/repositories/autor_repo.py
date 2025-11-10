from models.autor import Autor
from database import db, logger

class AutorRepository:
    @staticmethod
    def create_autor(nombre, edad):
        return Autor.create(
            nombre = nombre,
            edad = edad
        )

    @staticmethod
    def ingesta_multiple(lista_tuplas):
        with db.atomic():
            Autor.insert_many(lista_tuplas, fields=[
                Autor.nombre,
                Autor.edad
            ]).execute()

    @staticmethod
    def consulta_todos():
        for a in Autor.select():
            logger.info(f"id={a.id_autor}, nombre={a.nombre}, edad={a.edad}")