from models.genero import Genero
from models.libros import Libros
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
    
    @staticmethod
    def eliminar_genero(nombre):
        try:
            genero = Genero.get(Genero.nombre == nombre)
            Libros.update(id_genero=None).where(Libros.id_genero == genero).execute()
            genero.delete_instance() # tambien se puede hacer Genero.delete_instance(genero)
            logger.info("Genero borrado correctamente")
        except Genero.DoesNotExist:
            logger.info("No se ha encontrado ningun genero con ese nombre")