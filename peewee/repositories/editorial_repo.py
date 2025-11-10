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
        try:
            editorial = Editorial.get(Editorial.nombre == nombre)
            Libros.update(id_editorial=None).where(Libros.id_editorial == editorial).execute()
            editorial.delete_instance() # tambien se puede hacer Editorial.delete_instance(editorial)
            logger.info("Editorial borrada correctamente")
        except Editorial.DoesNotExist:
            logger.info("No se ha encontrado ninguna editorial con ese nombre")