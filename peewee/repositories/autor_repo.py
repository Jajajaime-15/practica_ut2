from models.autor import Autor
from models.libros import Libros
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


    @staticmethod
    def actualizar_autor(antiguo, nuevo):
        query = Autor.update(nombre = nuevo).where(Autor.nombre == antiguo)
        query.execute()
    
    @staticmethod
    def eliminar_autor(nombre):
        try:
            autor = Autor.get(Autor.nombre == nombre)
            Libros.update(id_autor=None).where(Libros.id_autor == autor).execute()
            autor.delete_instance() # tambien se puede hacer Autor.delete_instance(autor)
            logger.info("Autor borrado correctamente")
        except Autor.DoesNotExist:
            logger.info("No se ha encontrado ningun autor con ese nombre")