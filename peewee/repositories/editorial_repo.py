from models.editorial import Editorial
from models.libros import Libros
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

    @staticmethod
    def actualizar_editorial(antiguo, nuevo):
        query = Editorial.update(nombre = nuevo).where(Editorial.nombre == antiguo)
        query.execute()

    @staticmethod
    def eliminar_editorial(nombre):
        a = Editorial.select(Editorial.id_editorial).where(Editorial.nombre == nombre)
        #b = Libros.get(Editorial.id_editorial == a.id_editorial)

        #Libros.delete().where(Libros.id_editorial == a).execute()

        #Editorial.delete().where(Editorial.nombre == nombre).execute()