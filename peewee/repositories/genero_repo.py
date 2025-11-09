from models.genero import Genero
from database import db

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
        return Genero.select()