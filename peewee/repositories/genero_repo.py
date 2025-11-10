from models.genero import Genero
from database import db, logger

class GeneroRepository:
    @staticmethod
    def create_genero(nombre):
        return Genero.create(
            nombre = nombre
        )

    @staticmethod
    def ingesta_multiple(lista_tuplas):
        with db.atomic():
            Genero.insert_many(lista_tuplas, fields=[
                Genero.nombre
            ]).execute()


    @staticmethod
    def consulta_todos():
        for g in Genero.select():
            logger.info(f"id={g.id_genero}, nombre={g.nombre}")

    @staticmethod
    def actualizar_genero(antiguo, nuevo):
        query = Genero.update(nombre = nuevo).where(Genero.nombre == antiguo)
        query.execute()