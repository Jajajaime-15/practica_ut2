from models.editorial import Editorial
from database import db, logger

class EditorialRepository:
    @staticmethod
    def create_editorial(nombre):
        return Editorial.create(
            nombre = nombre
        )

    @staticmethod
    def ingesta_multiple(lista_tuplas):
        with db.atomic():
            Editorial.insert_many(lista_tuplas, fields=[
                Editorial.nombre
            ]).execute()
    
    @staticmethod
    def consulta_todos():
        for e in Editorial.select():
            logger.info(f"id={e.id_editorial}, nombre={e.nombre}")